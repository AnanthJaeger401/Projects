from django import forms
from .models import Student
from .models import Contact
from .models import Course
class StudentRegistrationForm(forms.ModelForm):
    course=forms.ModelChoiceField(queryset=Course.objects.all(), required=True)
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'address', 'phone_number']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 4}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']