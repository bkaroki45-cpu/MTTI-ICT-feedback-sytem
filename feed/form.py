from django import forms
from .models import ICTFeedback


class ICTFeedbackForm(forms.ModelForm):

    class Meta:
        model = ICTFeedback
        fields = "__all__"   # This automatically includes all model fields

        widgets = {

            # 1. General Experience
            'overall_experience': forms.Textarea(attrs={
                'placeholder': 'How would you rate your overall experience in the ICT Department?',
                'rows': 3,
            }),
            'recommendation': forms.Textarea(attrs={
                'placeholder': 'Would you recommend this course to other students?',
                'rows': 2,
            }),
            'training_satisfaction': forms.Textarea(attrs={
                'placeholder': 'Are you satisfied with the quality of training provided?',
                'rows': 2,
            }),

            # 2. Teaching & Lecturers
            'instructor_effectiveness': forms.Textarea(attrs={
                'placeholder': 'How effective are the instructors in delivering course content?',
                'rows': 3,
            }),
            'lesson_clarity': forms.Textarea(attrs={
                'placeholder': 'Are lessons clear and easy to understand?',
                'rows': 2,
            }),
            'practical_examples': forms.Textarea(attrs={
                'placeholder': 'Do lecturers provide enough practical examples?',
                'rows': 2,
            }),
            'student_participation': forms.Textarea(attrs={
                'placeholder': 'Are students encouraged to ask questions and participate?',
                'rows': 2,
            }),

            # 3. Course Content
            'industry_relevance': forms.Textarea(attrs={
                'placeholder': 'Is the course content relevant to current ICT industry standards?',
                'rows': 2,
            }),
            'module_structure': forms.Textarea(attrs={
                'placeholder': 'Are the modules well structured and organized?',
                'rows': 2,
            }),
            'most_useful_module': forms.Textarea(attrs={
                'placeholder': 'Which module did you find most useful?',
                'rows': 2,
            }),
            'module_improvement': forms.Textarea(attrs={
                'placeholder': 'Which module needs improvement?',
                'rows': 2,
            }),

            # 4. Practical Training
            'practical_sessions': forms.Textarea(attrs={
                'placeholder': 'Do you receive enough hands-on practical sessions?',
                'rows': 2,
            }),
            'lab_sessions_helpfulness': forms.Textarea(attrs={
                'placeholder': 'Are lab sessions helpful in understanding concepts?',
                'rows': 2,
            }),
            'project_application': forms.Textarea(attrs={
                'placeholder': 'Do projects help you apply what you learned?',
                'rows': 2,
            }),
            'industry_readiness': forms.Textarea(attrs={
                'placeholder': 'Do you feel industry-ready after completing the course?',
                'rows': 2,
            }),

            # 5. Facilities
            'computer_lab_rating': forms.Textarea(attrs={
                'placeholder': 'How would you rate the computer labs?',
                'rows': 2,
            }),
            'computer_functionality': forms.Textarea(attrs={
                'placeholder': 'Are computers functioning properly?',
                'rows': 2,
            }),
            'software_status': forms.Textarea(attrs={
                'placeholder': 'Is the software up to date?',
                'rows': 2,
            }),
            'internet_reliability': forms.Textarea(attrs={
                'placeholder': 'Is internet access reliable?',
                'rows': 2,
            }),

            # 6. Student Support
            'technical_support': forms.Textarea(attrs={
                'placeholder': 'Is technical support available when needed?',
                'rows': 2,
            }),
            'academic_guidance': forms.Textarea(attrs={
                'placeholder': 'Is academic guidance provided?',
                'rows': 2,
            }),
            'communication_effectiveness': forms.Textarea(attrs={
                'placeholder': 'Are communication channels effective?',
                'rows': 2,
            }),

            # 7. Improvements
            'department_improvement': forms.Textarea(attrs={
                'placeholder': 'What areas of the ICT department need improvement?',
                'rows': 3,
            }),
            'additional_courses': forms.Textarea(attrs={
                'placeholder': 'What additional courses would you like introduced?',
                'rows': 2,
            }),
            'training_quality_suggestions': forms.Textarea(attrs={
                'placeholder': 'Any suggestions to improve training quality?',
                'rows': 3,
            }),
            'additional_comments': forms.Textarea(attrs={
                'placeholder': 'Any additional comments?',
                'rows': 3,
            }),
        }