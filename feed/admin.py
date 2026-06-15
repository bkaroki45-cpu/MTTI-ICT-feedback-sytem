from django.contrib import admin
from django.http import HttpResponse

from .models import Announcement, Department, Event, EventFeedback, Feedback


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "unit_type", "contact_email", "allow_public_feedback", "is_active")
    list_filter = ("unit_type", "allow_public_feedback", "is_active")
    search_fields = ("name", "description", "staff_contact")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("department", "category", "feedback_type", "status", "created_at")
    list_display_links = ("department", "category")
    list_filter = ("department", "feedback_type", "category", "status", "created_at")
    search_fields = ("message", "admission_number", "student_class", "full_name", "guest_name", "smart_tags")
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    list_per_page = 25
    ordering = ("department__name", "-created_at")
    actions = ["mark_pending", "mark_resolved", "export_as_csv"]
    fieldsets = (
        ("Routing", {"fields": ("feedback_type", "category", "department", "status")}),
        ("Identity", {"fields": ("admission_number", "student_class", "full_name", "guest_name")}),
        ("Message", {"fields": ("message", "attachment", "admin_reply", "smart_tags")}),
        ("Timeline", {"fields": ("created_at", "updated_at")}),
    )

    @admin.action(description="Mark selected feedback as pending")
    def mark_pending(self, request, queryset):
        queryset.update(status=Feedback.PENDING)

    @admin.action(description="Mark selected feedback as resolved")
    def mark_resolved(self, request, queryset):
        queryset.update(status=Feedback.RESOLVED)

    @admin.action(description="Export selected feedback as CSV")
    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="feedback-export.csv"'
        response.write("created_at,department,type,category,status,message\n")
        for item in queryset.select_related("department"):
            department = item.department.name if item.department else "General"
            message = item.message.replace('"', '""').replace("\n", " ")
            response.write(f'{item.created_at},{department},{item.feedback_type},{item.category},{item.status},"{message}"\n')
        return response


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "starts_at", "department", "location", "is_published")
    list_filter = ("department", "starts_at", "is_published")
    search_fields = ("name", "description", "location")


@admin.register(EventFeedback)
class EventFeedbackAdmin(admin.ModelAdmin):
    list_display = ("event", "rating", "name", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("event__name", "name", "message")


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "announcement_type", "department", "published_at", "is_published")
    list_filter = ("announcement_type", "department", "is_published", "published_at")
    search_fields = ("title", "body")
