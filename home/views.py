from django.shortcuts import render
from .models import Project

def home_view(request):
    return render(request, 'home/home.html')

def about_view(request):
    return render(request, 'home/about.html')

def skills_view(request):
    return render(request, 'home/skills.html')

def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'home/projects.html', {'projects': projects})
