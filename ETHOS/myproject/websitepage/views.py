from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm

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
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us. We will get back to you shortly!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

