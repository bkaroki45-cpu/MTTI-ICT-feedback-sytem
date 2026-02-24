from django.db import models

class ICTFeedback(models.Model):

    YES_NO = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    RATING = [
        (1, '1 - Very Poor'),
        (2, '2 - Poor'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]

    # 1️⃣ General Experience
    overall_experience = models.IntegerField(choices=RATING, null=True, blank=True)
    recommendation = models.CharField(max_length=10, choices=YES_NO, blank=True)
    training_satisfaction = models.IntegerField(choices=RATING, null=True, blank=True)

    # 2️⃣ Teaching & Lecturers
    instructor_effectiveness = models.IntegerField(choices=RATING, null=True, blank=True)
    lesson_clarity = models.IntegerField(choices=RATING, null=True, blank=True)
    practical_examples = models.IntegerField(choices=RATING, null=True, blank=True)

    # 3️⃣ Course Content
    industry_relevance = models.IntegerField(choices=RATING, null=True, blank=True)
    most_useful_module = models.TextField(blank=True)

    # 4️⃣ Facilities
    computer_lab_rating = models.IntegerField(choices=RATING, null=True, blank=True)
    internet_reliability = models.IntegerField(choices=RATING, null=True, blank=True)

    # 5️⃣ Suggestions
    department_improvement = models.TextField(blank=True)
    additional_comments = models.TextField(blank=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"\n--- Feedback #{self.id} ---\n"
            f"Submitted at: {self.submitted_at}\n\n"

            f"=== General Experience ===\n"
            f"Overall Experience: {self.get_overall_experience_display()}\n"
            f"Recommendation: {self.recommendation}\n"
            f"Training Satisfaction: {self.get_training_satisfaction_display()}\n\n"

            f"=== Teaching & Lecturers ===\n"
            f"Instructor Effectiveness: {self.get_instructor_effectiveness_display()}\n"
            f"Lesson Clarity: {self.get_lesson_clarity_display()}\n"
            f"Practical Examples: {self.get_practical_examples_display()}\n\n"

            f"=== Course Content ===\n"
            f"Industry Relevance: {self.get_industry_relevance_display()}\n"
            f"Most Useful Module: {self.most_useful_module}\n\n"

            f"=== Facilities ===\n"
            f"Computer Lab Rating: {self.get_computer_lab_rating_display()}\n"
            f"Internet Reliability: {self.get_internet_reliability_display()}\n\n"

            f"=== Suggestions ===\n"
            f"Department Improvement: {self.department_improvement}\n"
            f"Additional Comments: {self.additional_comments}\n"
        )