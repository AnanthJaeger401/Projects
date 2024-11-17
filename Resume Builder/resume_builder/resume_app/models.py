from django.db import models
from month.models import MonthField



proficiencyoptions=[('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),]

class Resume(models.Model):
    user = models.CharField(max_length=255, default='user1')
    name=models.CharField(max_length=255, default='Your Name')
    email=models.EmailField(default='abc@email.com')
    Phone_No=models.PositiveBigIntegerField(default=9663768094)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    resume_template = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="work_experiences")
    job_title = models.CharField(max_length=255, null=True)
    company = models.CharField(max_length=255, null=True)
    start_date = MonthField(null=True)
    end_date = MonthField(null=True, blank=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.job_title

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="educations")
    institute = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_date = MonthField()
    end_date = MonthField(null=True, blank=True)
    gpapercentage=models.FloatField(default=0.0)

    def __str__(self):
        return self.degree

class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=255)
    proficiency=models.CharField(max_length=50, choices=proficiencyoptions, default='Beginner')

    def __str__(self):
        return self.name

class Language(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="languages")
    name = models.CharField(max_length=255)
    proficiency = models.CharField(max_length=50, choices=proficiencyoptions, default='Beginner')

    def __str__(self):
        return self.name

class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="projects")
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Achievement(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="achievements")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
