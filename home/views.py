from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request):
    return HttpResponse("<h1>Hello, I’m Shabin!</h1><p>Welcome to my portfolio site.</p>")