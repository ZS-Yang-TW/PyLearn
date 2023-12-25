from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse  
from django.conf.urls.static import static
from django.conf import settings

from .views import home,  course_page, signout, check_out
from .views import SignupView, LoginView
urlpatterns = [
    path("", home, name = "Home Page"),
    path("signup", SignupView.as_view(), name = "Signup Page"),
    path("login", LoginView.as_view(), name = "Login Page"),
    path("logout", signout, name = "Logout Page"),
    path('courses/<str:slug>', course_page, name = "Course Page"),
    path('check-out/<str:slug>', check_out, name = "Course Page"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
