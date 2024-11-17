from django.urls import path
from .views import *

app_name='resume'

urlpatterns = [
    path('create/', create_resume, name='create_resume'),
    path('', homepage, name='homepage'),
    path('logout', logout_view),
    path("select-template/", select_template_page, name="select_template_page"),
    path("select-template/<int:template_id>/", select_template, name="select_template"),
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('resume/<int:resume_id>/', resume_detail, name='resume_detail'),
]
