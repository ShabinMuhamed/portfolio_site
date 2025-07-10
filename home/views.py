from django.shortcuts import render,get_object_or_404
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

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'home/project_detail.html', {'project': project})
