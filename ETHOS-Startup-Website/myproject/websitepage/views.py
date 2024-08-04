from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentRegistrationForm, ContactForm
from .models import Course

def homepage(request):
    return render(request, 'homepage.html')

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_success')
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def register_success(request):
    return render(request, 'register_success.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us. We will get back to you shortly!')
            return redirect('thank_you')  # Redirect to thank_you page
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

def courses_list(request):
    c1 = Course.objects.all()
    return render(request, 'courses.html', {'courses': c1})

def about(request):
    return render(request, 'aboutus.html')
