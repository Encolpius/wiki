from django.shortcuts import render
from .models import Sessions

def home(request):
    context = {
        'sessions': Sessions.objects.all()
    }
    return render(request, "saltmarsh/home.html", context)

def about(request):
    return render(request, "saltmarsh/about.html", { 'title': 'About'})