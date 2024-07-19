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

