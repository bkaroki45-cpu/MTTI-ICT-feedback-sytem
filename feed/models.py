from django.db import models

from django.db import models


class ICTFeedback(models.Model):

    # 1. General Experience
    overall_experience = models.TextField(blank=True)
    recommendation = models.TextField(blank=True)
    training_satisfaction = models.TextField(blank=True)

    # 2. Teaching & Lecturers
    instructor_effectiveness = models.TextField(blank=True)
    lesson_clarity = models.TextField(blank=True)
    practical_examples = models.TextField(blank=True)
    student_participation = models.TextField(blank=True)

    # 3. Course Content & Curriculum
    industry_relevance = models.TextField(blank=True)
    module_structure = models.TextField(blank=True)
    most_useful_module = models.TextField(blank=True)
    module_improvement = models.TextField(blank=True)

    # 4. Practical Training
    practical_sessions = models.TextField(blank=True)
    lab_sessions_helpfulness = models.TextField(blank=True)
    project_application = models.TextField(blank=True)
    industry_readiness = models.TextField(blank=True)

    # 5. Facilities & Resources
    computer_lab_rating = models.TextField(blank=True)
    computer_functionality = models.TextField(blank=True)
    software_status = models.TextField(blank=True)
    internet_reliability = models.TextField(blank=True)

    # 6. Student Support
    technical_support = models.TextField(blank=True)
    academic_guidance = models.TextField(blank=True)
    communication_effectiveness = models.TextField(blank=True)

    # 7. Improvement & Suggestions
    department_improvement = models.TextField(blank=True)
    additional_courses = models.TextField(blank=True)
    training_quality_suggestions = models.TextField(blank=True)
    additional_comments = models.TextField(blank=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    
    
def __str__(self):
    return (
        f"\n--- Feedback #{self.id} ---\n"
        f"Submitted at: {self.submitted_at}\n\n"

        f"Overall Experience: {self.overall_experience}\n"
        f"Recommendation: {self.recommendation}\n"
        f"Training Satisfaction: {self.training_satisfaction}\n\n"

        f"Instructor Effectiveness: {self.instructor_effectiveness}\n"
        f"Lesson Clarity: {self.lesson_clarity}\n"
        f"Practical Examples: {self.practical_examples}\n"
        f"Student Participation: {self.student_participation}\n\n"

        f"Industry Relevance: {self.industry_relevance}\n"
        f"Module Structure: {self.module_structure}\n"
        f"Most Useful Module: {self.most_useful_module}\n"
        f"Module Improvement: {self.module_improvement}\n\n"

        f"Practical Sessions: {self.practical_sessions}\n"
        f"Lab Helpfulness: {self.lab_sessions_helpfulness}\n"
        f"Project Application: {self.project_application}\n"
        f"Industry Readiness: {self.industry_readiness}\n\n"

        f"Computer Lab Rating: {self.computer_lab_rating}\n"
        f"Computer Functionality: {self.computer_functionality}\n"
        f"Software Status: {self.software_status}\n"
        f"Internet Reliability: {self.internet_reliability}\n\n"

        f"Technical Support: {self.technical_support}\n"
        f"Academic Guidance: {self.academic_guidance}\n"
        f"Communication Effectiveness: {self.communication_effectiveness}\n\n"

        f"Department Improvement: {self.department_improvement}\n"
        f"Additional Courses: {self.additional_courses}\n"
        f"Training Quality Suggestions: {self.training_quality_suggestions}\n"
        f"Additional Comments: {self.additional_comments}\n"
    )