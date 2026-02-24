from django import forms
from .models import ICTFeedback

class ICTFeedbackForm(forms.ModelForm):
    class Meta:
        model = ICTFeedback
        fields = '__all__'

        widgets = {
            'recommendation': forms.RadioSelect,
            'overall_experience': forms.RadioSelect,
            'training_satisfaction': forms.RadioSelect,
            'instructor_effectiveness': forms.RadioSelect,
            'lesson_clarity': forms.RadioSelect,
            'practical_examples': forms.RadioSelect,
            'industry_relevance': forms.RadioSelect,
            'computer_lab_rating': forms.RadioSelect,
            'internet_reliability': forms.RadioSelect,
            'most_useful_module': forms.Textarea(attrs={'rows': 3}),
            'department_improvement': forms.Textarea(attrs={'rows': 3}),
            'additional_comments': forms.Textarea(attrs={'rows': 3}),
        }