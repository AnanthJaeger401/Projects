from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Resume)
admin.site.register(WorkExperience)
admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Achievement)