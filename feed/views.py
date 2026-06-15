from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .form import EventFeedbackForm, FeedbackForm
from .models import Department, Event, Feedback


def seed_departments():
    departments = [
        ("Agriculture", "agriculture", Department.CORE, "Agriculture training, farm practice, agribusiness, and food production programs."),
        ("Automotive Engineering", "automotive-engineering", Department.CORE, "Vehicle systems, diagnostics, workshop practice, and transport technology."),
        ("Business", "business", Department.CORE, "Accounting, entrepreneurship, procurement, management, and office administration."),
        ("Building and Civil Engineering", "building-and-civil-engineering", Department.CORE, "Construction, surveying, masonry, plumbing, and civil works training."),
        ("Electrical and Electronics Engineering", "electrical-and-electronics-engineering", Department.CORE, "Power systems, electronics, installation, control, and maintenance."),
        ("Fashion Design and Clothing Technology", "fashion-design-and-clothing-technology", Department.CORE, "Garment construction, design, textile work, and apparel production."),
        ("Hospitality and Tourism", "hospitality-and-tourism", Department.CORE, "Food production, service, accommodation, travel, and tourism operations."),
        ("Information and Communication Technology", "information-and-communication-technology", Department.CORE, "Computing, networking, programming, digital literacy, and systems support."),
        ("Kitchen / Catering", "kitchen-catering", Department.SUPPORT, "Meals, catering service, hygiene, and dining support for the institute."),
        ("Library", "library", Department.SUPPORT, "Learning resources, research support, circulation, and study spaces."),
        ("Health Services", "health-services", Department.SUPPORT, "Student and staff health, first aid, wellness, and referrals."),
        ("Hostels", "hostels", Department.SUPPORT, "Accommodation, room allocation, welfare, and boarding facilities."),
        ("Games & Sports", "games-sports", Department.SUPPORT, "Sports programs, recreation, competitions, and talent development."),
        ("Entertainment", "entertainment", Department.SUPPORT, "Student activities, talent shows, social events, and campus culture."),
        ("Security Department", "security-department", Department.SUPPORT, "Campus safety, access control, incident reporting, and emergency response."),
        ("Staff Office", "staff-office", Department.SUPPORT, "Staff coordination, welfare, records, and institutional support."),
        ("Student Council (MATTISU)", "student-council-mattisu", Department.SUPPORT, "Student leadership, representation, welfare, and engagement."),
        ("Guidance and Counselling", "guidance-and-counselling", Department.SUPPORT, "Counselling, mentorship, mental wellness, and career guidance."),
    ]
    for name, slug, unit_type, description in departments:
        Department.objects.get_or_create(
            slug=slug,
            defaults={"name": name, "unit_type": unit_type, "description": description},
        )


def home(request):
    seed_departments()
    context = {
        "departments_count": Department.objects.filter(is_active=True).count(),
        "feedback_count": Feedback.objects.count(),
        "events": Event.objects.filter(is_published=True)[:3],
    }
    return render(request, "feed/index.html", context)


def departments(request):
    seed_departments()
    context = {
        "core_departments": Department.objects.filter(unit_type=Department.CORE, is_active=True),
        "support_units": Department.objects.filter(unit_type=Department.SUPPORT, is_active=True),
    }
    return render(request, "feed/departments/index.html", context)


def department_detail(request, slug):
    department = get_object_or_404(Department, slug=slug, is_active=True)
    permitted_feedback = department.feedback_items.filter(status=Feedback.RESOLVED, department__allow_public_feedback=True)[:8]
    return render(request, "feed/departments/detail.html", {"department": department, "permitted_feedback": permitted_feedback})


def feedback(request, department_slug=None):
    seed_departments()
    department = None
    if department_slug:
        department = get_object_or_404(Department, slug=department_slug, is_active=True)

    if request.method == "POST":
        form = FeedbackForm(request.POST, request.FILES, department=department)
        if form.is_valid():
            form.save()
            return redirect("message")
    else:
        form = FeedbackForm(department=department)

    return render(request, "feed/feedback.html", {"form": form, "department": department})


def message(request):
    return render(request, "feed/message.html")


def events(request):
    return render(request, "feed/events.html", {"events": Event.objects.filter(is_published=True)})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk, is_published=True)
    if request.method == "POST":
        form = EventFeedbackForm(request.POST)
        if form.is_valid():
            event_feedback = form.save(commit=False)
            event_feedback.event = event
            event_feedback.save()
            return redirect("event_detail", pk=event.pk)
    else:
        form = EventFeedbackForm()
    return render(request, "feed/event_detail.html", {"event": event, "form": form})


def admin_required(user):
    return user.is_staff


@user_passes_test(admin_required)
def institutional_dashboard(request):
    feedback_by_department = Feedback.objects.values("department__name").annotate(total=Count("id")).order_by("-total")[:8]
    feedback_by_category = Feedback.objects.values("category").annotate(total=Count("id")).order_by("-total")
    context = {
        "total_feedback": Feedback.objects.count(),
        "pending_feedback": Feedback.objects.filter(status=Feedback.PENDING).count(),
        "resolved_feedback": Feedback.objects.filter(status=Feedback.RESOLVED).count(),
        "feedback_by_department": feedback_by_department,
        "feedback_by_category": feedback_by_category,
        "recent_feedback": Feedback.objects.select_related("department")[:10],
    }
    return render(request, "feed/admin_dashboard.html", context)
