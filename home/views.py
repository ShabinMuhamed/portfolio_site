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

def contact_view(request):
    success = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # For now, just print to console (later you can save/send this)
        print("New message:")
        print(f"From: {name} <{email}>")
        print("Message:", message)

        success = True

    return render(request, 'home/contact.html', {'success': success})
