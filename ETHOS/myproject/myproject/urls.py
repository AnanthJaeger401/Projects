"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from websitepage.views import courses_list,homepage,contact_view,register,register_success,about, thank_you

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('register/', register, name='register'),
    path('contact/', contact_view, name='contact'),
    path('register_success/', register_success, name='register_success'),
    path('courses/', courses_list, name='courses_list'),
    path('aboutus/', about, name='about'),
    path('thank-you/', thank_you, name='thank_you'),

]
