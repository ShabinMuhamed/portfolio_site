from django.shortcuts import render,get_object_or_404
from .models import Project
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()
    message_sent = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f'New Contact Form Submission from {name}'
            full_message = f'From: {name} <{email}>\n\nMessage:\n{message}'

            send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_RECEIVER_EMAIL])
            message_sent = True

    return render(request, 'home/contact.html', {'form': form, 'message_sent': message_sent})

def home_view(request):
    return render(request, 'home/home.html')

def about_view(request):
    return render(request, 'home/about.html')

def skills_view(request):
    return render(request, 'home/skills.html')

def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'home/projects.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'home/project_detail.html', {'project': project})
