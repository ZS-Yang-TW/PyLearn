from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse  

from .views import home

urlpatterns = [
    path("", home, name = "Home Page"),
]
