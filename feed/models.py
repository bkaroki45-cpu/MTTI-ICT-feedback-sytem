from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Department(models.Model):
    CORE = "core"
    SUPPORT = "support"

    UNIT_TYPE_CHOICES = [
        (CORE, "Core Department"),
        (SUPPORT, "Support / Institutional Unit"),
    ]

    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True)
    unit_type = models.CharField(max_length=20, choices=UNIT_TYPE_CHOICES, default=CORE)
    description = models.TextField()
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=40, blank=True)
    staff_contact = models.CharField(max_length=160, blank=True)
    allow_public_feedback = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["unit_type", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("department_detail", kwargs={"slug": self.slug})


class Feedback(models.Model):
    ANONYMOUS = "anonymous"
    STUDENT = "student"
    STAFF = "staff"
    GUEST = "guest"

    FEEDBACK_TYPE_CHOICES = [
        (ANONYMOUS, "Anonymous Feedback"),
        (STUDENT, "Identified Feedback (Student)"),
        (STAFF, "Identified Feedback (Staff)"),
        (GUEST, "Guest Feedback"),
    ]

    COMPLAINT = "complaint"
    SUGGESTION = "suggestion"
    APPRECIATION = "appreciation"
    REPORT = "report"
    OTHER = "other"

    CATEGORY_CHOICES = [
        (COMPLAINT, "Complaint"),
        (SUGGESTION, "Suggestion"),
        (APPRECIATION, "Appreciation"),
        (REPORT, "Report"),
        (OTHER, "Other"),
    ]

    PENDING = "pending"
    IN_REVIEW = "in_review"
    RESOLVED = "resolved"

    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (IN_REVIEW, "In Review"),
        (RESOLVED, "Resolved"),
    ]

    feedback_type = models.CharField(max_length=20, choices=FEEDBACK_TYPE_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="feedback_items",
    )
    message = models.TextField()
    attachment = models.FileField(upload_to="feedback_attachments/", blank=True)

    admission_number = models.CharField(max_length=40, blank=True)
    student_class = models.CharField("Class", max_length=80, blank=True)
    full_name = models.CharField(max_length=120, blank=True)
    guest_name = models.CharField(max_length=120, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    admin_reply = models.TextField(blank=True)
    smart_tags = models.CharField(
        max_length=255,
        blank=True,
        help_text="Comma-separated tags generated manually or by a future AI classifier.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        target = self.department.name if self.department else "General"
        return f"{self.get_category_display()} for {target} ({self.get_feedback_type_display()})"

    @property
    def is_identified(self):
        return self.feedback_type in {self.STUDENT, self.STAFF, self.GUEST}


class Event(models.Model):
    name = models.CharField(max_length=160)
    description = models.TextField()
    image = models.ImageField(upload_to="event_images/", blank=True)
    starts_at = models.DateTimeField(default=timezone.now)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="events",
    )
    location = models.CharField(max_length=160)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_events",
    )
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["starts_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})


class EventFeedback(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="feedback_items")
    name = models.CharField(max_length=120, blank=True)
    rating = models.PositiveSmallIntegerField(
        choices=[(value, f"{value} Star{'s' if value > 1 else ''}") for value in range(1, 6)],
        null=True,
        blank=True,
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Feedback for {self.event.name}"


class Announcement(models.Model):
    NOTICE = "notice"
    FEES = "fees"
    EXAMS = "exams"
    ALERT = "alert"

    ANNOUNCEMENT_TYPE_CHOICES = [
        (NOTICE, "School Notice"),
        (FEES, "Fee Update"),
        (EXAMS, "Exam Schedule"),
        (ALERT, "General Alert"),
    ]

    title = models.CharField(max_length=180)
    body = models.TextField()
    announcement_type = models.CharField(max_length=20, choices=ANNOUNCEMENT_TYPE_CHOICES, default=NOTICE)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="announcements",
    )
    published_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title


# Backward-compatible alias for older imports/migrations that referenced ICTFeedback.
ICTFeedback = Feedback
