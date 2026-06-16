from django import forms

from .models import Department, EventFeedback, Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            "feedback_type",
            "category",
            "department",
            "admission_number",
            "student_class",
            "full_name",
            "guest_name",
            "message",
            "attachment",
        ]
        widgets = {
            "feedback_type": forms.RadioSelect,
            "category": forms.Select,
            "department": forms.Select,
            "message": forms.Textarea(attrs={"rows": 5, "placeholder": "Describe the issue, suggestion, report, or appreciation clearly."}),
        }

    def __init__(self, *args, **kwargs):
        department = kwargs.pop("department", None)
        super().__init__(*args, **kwargs)
        self.fields["department"].queryset = Department.objects.filter(is_active=True)
        self.fields["message"].required = True
        self.fields["category"].required = False
        self.fields["department"].required = False
        self.fields["attachment"].required = False

        if department:
            self.fields["department"].initial = department

        for field in self.fields.values():
            widget = field.widget
            if not isinstance(widget, forms.RadioSelect):
                widget.attrs.setdefault("class", "form-control")

    def clean(self):
        cleaned_data = super().clean()
        feedback_type = cleaned_data.get("feedback_type")

        if feedback_type in {Feedback.ANONYMOUS, Feedback.GUEST}:
            cleaned_data["category"] = Feedback.OTHER
            cleaned_data["department"] = None
            cleaned_data["admission_number"] = ""
            cleaned_data["student_class"] = ""
            cleaned_data["full_name"] = ""

        if feedback_type == Feedback.ANONYMOUS:
            cleaned_data["guest_name"] = ""

        if feedback_type == Feedback.GUEST and not cleaned_data.get("guest_name"):
            self.add_error("guest_name", "Name is required for guest feedback.")

        if feedback_type == Feedback.STUDENT:
            if not cleaned_data.get("category"):
                self.add_error("category", "Category is required for student feedback.")
            if not cleaned_data.get("admission_number"):
                self.add_error("admission_number", "Admission number is required for student feedback.")
            if not cleaned_data.get("student_class"):
                self.add_error("student_class", "Class is required for student feedback.")
            if not cleaned_data.get("department"):
                self.add_error("department", "Department is required for student feedback.")

        if feedback_type == Feedback.STAFF:
            if not cleaned_data.get("category"):
                self.add_error("category", "Category is required for staff feedback.")
            if not cleaned_data.get("full_name"):
                self.add_error("full_name", "Full name is required for staff feedback.")
            if not cleaned_data.get("department"):
                self.add_error("department", "Department is required for staff feedback.")

        return cleaned_data


class EventFeedbackForm(forms.ModelForm):
    class Meta:
        model = EventFeedback
        fields = ["name", "rating", "message"]
        widgets = {
            "rating": forms.RadioSelect,
            "message": forms.Textarea(attrs={"rows": 4, "placeholder": "Share your event experience."}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["message"].required = True
        self.fields["name"].required = False
        for field in self.fields.values():
            if not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs.setdefault("class", "form-control")


# Backward-compatible name for existing imports.
ICTFeedbackForm = FeedbackForm
