from django.shortcuts import render, HttpResponse
from .models import Course

def home(request):
    courses = Course.objects.all()
    
    return render(request, "courses/home.html", {"courses": courses})