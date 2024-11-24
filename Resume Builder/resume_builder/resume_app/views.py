from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import (
    ResumeForm, 
    WorkExperienceFormset, 
    EducationFormset, 
    SkillFormset, 
    LanguageFormset, 
    ProjectFormset, 
    AchievementFormset
)
from .models import Resume
import json
import google.generativeai as genai
import re
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
from docx import Document
from django.template.loader import render_to_string
googleapi='AIzaSyBY0l94WFrhONxJTqIkZy2sFSnkieSL7y4'

@login_required
def create_resume(request):
    selected_template = request.session.get('selected_template')
    print(selected_template)
    if request.method == 'POST':
        resume_form = ResumeForm(request.POST)
        
        # Initialize all formsets with POST data but don't attach instance yet
        work_experience_formset = WorkExperienceFormset(
            request.POST, 
            prefix='workexperience'
        )
        education_formset = EducationFormset(
            request.POST, 
            prefix='education'
        )
        skill_formset = SkillFormset(
            request.POST, 
            prefix='skill'
        )
        language_formset = LanguageFormset(
            request.POST, 
            prefix='language'
        )
        project_formset = ProjectFormset(
            request.POST, 
            prefix='project'
        )
        achievement_formset = AchievementFormset(
            request.POST, 
            prefix='achievement'
        )
        
        if resume_form.is_valid():
            resume = resume_form.save(commit=False)
            resume.user=request.user
            resume.resume_template = selected_template
            resume.save()
            
            # Now attach the resume instance to each formset
            work_experience_formset = WorkExperienceFormset(
                request.POST, 
                prefix='workexperience',
                instance=resume
            )
            education_formset = EducationFormset(
                request.POST, 
                prefix='education',
                instance=resume
            )
            skill_formset = SkillFormset(
                request.POST, 
                prefix='skill',
                instance=resume
            )
            language_formset = LanguageFormset(
                request.POST, 
                prefix='language',
                instance=resume
            )
            project_formset = ProjectFormset(
                request.POST, 
                prefix='project',
                instance=resume
            )
            achievement_formset = AchievementFormset(
                request.POST, 
                prefix='achievement',
                instance=resume
            )
            
            if (
                work_experience_formset.is_valid() and
                education_formset.is_valid() and
                skill_formset.is_valid() and
                language_formset.is_valid() and
                project_formset.is_valid() and
                achievement_formset.is_valid()
            ):
                # Save all formsets
                work_experience_formset.save()
                education_formset.save()
                skill_formset.save()
                language_formset.save()
                project_formset.save()
                achievement_formset.save()

                data={
                'Resume':resume_form.cleaned_data,
                'WorkExperience':work_experience_formset.cleaned_data,
                'Education':education_formset.cleaned_data,
                'Skill':skill_formset.cleaned_data,
                'Language':language_formset.cleaned_data,
                'Project':project_formset.cleaned_data,
                'Achievement':achievement_formset.cleaned_data}

                import os
                os.environ["API_KEY"] = 'AIzaSyCsC94-BjwhTY1ZVjb8vRXV8JzIlNmGqug'
                genai.configure(api_key=os.environ["API_KEY"])
                model = genai.GenerativeModel('gemini-1.5-flash-latest')

                prompt = f"""
                Create a professional resume using the following information in a structured JSON format, with each section clearly defined. The response should include the following sections:
                1. Personal Information (with name, email, phone number)
                2. Work Experience (with job title, company, start and end date, description)
                3. Education (with institute, degree, start and end date, GPA)
                4. Skills (with skill name and proficiency level)
                5. Languages (with language name and proficiency level)
                6. Projects (with project name and description)
                7. Achievements (with title and description)

                Personal Information:
                Name: {data['Resume']['name']}
                Email: {data['Resume']['email']}
                Phone: {data['Resume']['Phone_No']}

                Work Experience:
                {data['WorkExperience']}

                Education:
                {data['Education']}

                Skills:
                {data['Skill']}

                Languages:
                {data['Language']}

                Projects:
                {data['Project']}

                Achievements:
                {data['Achievement']}

                The resume should be structured with the following fields:
                1. header (containing name, email, and phone number)
                2. professionalsummary (a brief overview of the professional experience based on work history)
                3. workexperience (list of positions held, with key responsibilities and achievements highlighted) (should be empty if the value given is empty or null)
                4. education (including degrees, institutes, and dates)
                5. skills (list of skills with proficiency levels)
                6. languages (languages spoken and their proficiency)
                7. projects (list of significant projects worked on)
                8. achievements (any notable achievements)

                Make sure the resume is formatted in JSON with the fields as described above. The response should be human-readable, easy to parse, and formatted for easy rendering in a template.
                """
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(prompt)
                response_text=response.text
                json_match = re.search(r'({.*})', response_text, re.DOTALL)
                response=json.loads(json_match.group(1))
                print(response)
                
                val={
                'resume': response["header"],  # This provides access to the 'Header' dictionary
                'name': response["header"]["name"],
                'email': response["header"]["email"],
                'phone': response["header"]["phone"],
                'summary': response["professionalsummary"],
                'work_experiences': response["workexperience"],
                'educations': response["education"],
                'skills': response["skills"],
                'languages': response["languages"],
                'projects': response["projects"],
                'achievements': response["achievements"],
            }
                
                if request.GET.get('download') == 'pdf':
                    html = render_to_string(f'resume_{resume.resume_template}.html', context)
                    response = HttpResponse(content_type='application/pdf')
                    response['Content-Disposition'] = f'attachment; filename="{resume.title}_resume.pdf"'
                    pisa.CreatePDF(html, dest=response)
                    return response
                
                if selected_template==1:
                    return render(request, 'resume_1.html', val)
                elif selected_template==2:
                    return render(request, 'resume_2.html', val)
                elif selected_template==3:
                    return render(request, 'resume_3.html', val)  # Use named URL pattern
    else:
        resume_form = ResumeForm()
        # Initialize empty formsets with prefixes
        work_experience_formset = WorkExperienceFormset(
            prefix='workexperience'
        )
        education_formset = EducationFormset(
            prefix='education'
        )
        skill_formset = SkillFormset(
            prefix='skill'
        )
        language_formset = LanguageFormset(
            prefix='language'
        )
        project_formset = ProjectFormset(
            prefix='project'
        )
        achievement_formset = AchievementFormset(
            prefix='achievement'
        )
    
    context = {
        'resume_form': resume_form,
        'work_experience_formset': work_experience_formset,
        'education_formset': education_formset,
        'skill_formset': skill_formset,
        'language_formset': language_formset,
        'project_formset': project_formset,
        'achievement_formset': achievement_formset,
        'template': selected_template,
    }
    
    return render(request, 'create_resume.html', context)

def homepage(request):
    return render(request, 'homepage.html')
@login_required
def logout_view(request):
    logout(request)
    return redirect("/")

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@login_required
# View to display template selection page
def select_template_page(request):
    templates = [
        {"id": 1, "name": "Template 1", "preview_image": "/static/images/template1.png"},
        {"id": 2, "name": "Template 2", "preview_image": "/static/images/template2.png"},
        {"id": 3, "name": "Template 3", "preview_image": "/static/images/template3.png"},
    ]
    return render(request, "choosetemplate.html", {"templates": templates})

# View to handle template selection
@csrf_exempt
def select_template(request, template_id):
    if request.method == "POST":
        request.session["selected_template"] = template_id
        return JsonResponse({"success": True})
    return JsonResponse({"error": "Invalid request"}, status=400)

@login_required
def user_dashboard(request):
    # Get the current user
    user = request.user
    
    # Fetch resumes created by the user
    resumes = Resume.objects.filter(user=user)
    
    context = {
        'user': user,
        'resumes': resumes,
    }
    return render(request, 'dashboard.html', context)

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resume

@login_required
def resume_detail(request, resume_id):
    # Retrieve the resume object or return 404 if not found
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    
    # Structure the context for rendering
    context = {
        'name': resume.name,
        'email': resume.email,
        'phone': resume.Phone_No,
        'summary': resume.summary,  # Corrected field name
        'work_experiences': resume.work_experiences.all(),  # Using related_name
        'educations': resume.educations.all(),  # Using related_name
        'skills': resume.skills.all(),  # Using related_name
        'languages': resume.languages.all(),  # Using related_name
        'projects': resume.projects.all(),  # Using related_name
        'achievements': resume.achievements.all(),  # Using related_name
    }
    
    if request.GET.get('download') == 'pdf':
        html = render_to_string(f'resume_{resume.resume_template}.html', context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{resume.title}_resume.pdf"'
        pisa.CreatePDF(html, dest=response)
        return response

    # Render the appropriate template based on the resume's selected template
    if resume.resume_template == 1:  # Corrected field name
        return render(request, 'resume_1.html', context)
    elif resume.resume_template == 2:
        return render(request, 'resume_2.html', context)
    elif resume.resume_template == 3:
        return render(request, 'resume_3.html', context)
    else:
        # Fallback in case of no valid template
        return render(request, 'resume_1.html', context)

