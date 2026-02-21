from django.db import models

class ICTFeedback(models.Model):
    overall_experience = models.TextField(blank=True)
    facilities_satisfaction = models.TextField(blank=True)
    instructor_effectiveness = models.TextField(blank=True)
    useful_courses = models.TextField(blank=True)
    improvement_areas = models.TextField(blank=True)
    additional_comments = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return (
        f"Feedback #{self.id}\n"
        f"Overall Experience: {self.overall_experience}\n"
        f"Facilities Satisfaction: {self.facilities_satisfaction}\n"
        f"Instructor Effectiveness: {self.instructor_effectiveness}\n"
        f"Useful Courses: {self.useful_courses}\n"
        f"Improvement Areas: {self.improvement_areas}\n"
        f"Additional Comments: {self.additional_comments}"
    )