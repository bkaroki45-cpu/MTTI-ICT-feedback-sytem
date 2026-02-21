from django import forms
from .models import ICTFeedback

class ICTFeedbackForm(forms.ModelForm):
    class Meta:
        model = ICTFeedback
        fields = [
            'overall_experience',
            'facilities_satisfaction',
            'instructor_effectiveness',
            'useful_courses',
            'improvement_areas',
            'additional_comments'
        ]

        
        widgets = {
            'overall_experience': forms.Textarea(attrs={
                'placeholder': 'Write your overall experience with '
                'the ICT department...',
                'rows': 3,
            }),
            'facilities_satisfaction': forms.Textarea(attrs={
                'placeholder': 'How satisfied are you with '
                'the ICT facilities (labs, computers, software)?',
                'rows': 3,
            }),
            'instructor_effectiveness': forms.Textarea(attrs={
                'placeholder': 'How effective are the ICT instructors/'
                'lecturers in teaching?',
                'rows': 3,
            }),
            'useful_courses': forms.Textarea(attrs={
                'placeholder': 'Which ICT courses/topics do '
                'you find most useful?',
                'rows': 2,
            }),
            'improvement_areas': forms.Textarea(attrs={
                'placeholder': 'Which areas of the ICT department '
                'need improvement?',
                'rows': 2,
            }),
            'additional_comments': forms.Textarea(attrs={
                'placeholder': 'Any additional comments or'
                ' suggestions...',
                'rows': 4,
            }),
        }