from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.views import View

from .models import Course, Video
from .forms import RegisterForm, LoginForm

class SignupView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "courses/signup.html", {"form": form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect("/login")
            pass
    
        return render(request, "courses/signup.html", {"form": form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "courses/login.html", {"form": form})
    
    def post(self, request):
        form = LoginForm(request = request, data = request.POST)
        if form.is_valid():
            return redirect("/")
        return render(request, "courses/login.html", {"form": form})
    
def home(request):
    courses = Course.objects.all()
    return render(request, "courses/home.html", {"courses": courses})

# 使用 signout 而不是 logout，是因為 logout 是 Django 內建的函式
def signout(request):
    logout(request)
    return redirect("/")

def course_page(request, slug):
    course = Course.objects.get(slug = slug)
    videos = course.video_set.all().order_by("serial_number")
    
    serial_number = request.GET.get("lecture", None)
    if serial_number == None:
        serial_number = 1
    video = Video.objects.get(course = course, serial_number = serial_number)
    
    if (request.user.is_authenticated) and (video.is_preview == False):
        return redirect("/login")
    
    context = {
        "course": course,
        "video": video,
        "videos": videos
    }
    
    return render(request, "courses/course_page.html", context)

def check_out(request, slug):
    course = Course.objects.get(slug = slug)
    if not request.user.is_authenticated:
        return redirect("/login")
    context = {
        "course": course
    }
    
    return render(request, "courses/check-out.html", context)