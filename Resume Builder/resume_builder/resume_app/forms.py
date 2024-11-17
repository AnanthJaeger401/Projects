from django import forms
from django.forms import inlineformset_factory
from .models import Resume, WorkExperience, Education, Skill, Language, Project, Achievement

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name','email','Phone_No','title','summary')

# Inline formsets for each related model
WorkExperienceFormset = inlineformset_factory(
    Resume, WorkExperience,
    fields='__all__',
    extra=1,
    can_delete=True,
    #  widgets = {
    #         'start_date': forms.DateInput(attrs={'type': 'month', 'placeholder': 'YYYY-MM'}),
    #         'end_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM'}),
    #     }
)

EducationFormset = inlineformset_factory(
    Resume, Education,
    fields='__all__',
    extra=1,
    can_delete=True,
    #  widgets = {
    #         'start_date': forms.DateInput(attrs={'type': 'month', 'placeholder': 'YYYY-MM-DD'}),
    #         'end_date': forms.DateInput(attrs={'type': 'month', 'placeholder': 'YYYY-MM-DD'}),
    #     }
)

SkillFormset = inlineformset_factory(
    Resume, Skill,
    fields='__all__',
    extra=1,
    can_delete=True
)

LanguageFormset = inlineformset_factory(
    Resume, Language,
    fields='__all__',
    extra=1,
    can_delete=True
)

ProjectFormset = inlineformset_factory(
    Resume, Project,
    fields='__all__',
    extra=1,
    can_delete=True
)

AchievementFormset = inlineformset_factory(
    Resume, Achievement,
    fields='__all__',
    extra=1,
    can_delete=True
)
