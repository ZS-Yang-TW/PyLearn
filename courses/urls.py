from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse  
from django.conf.urls.static import static
from PyLearn.settings import MEDIA_ROOT, MEDIA_URL

from .views import home

urlpatterns = [
    path("", home, name = "Home Page"),
] + static(MEDIA_URL, document_root = MEDIA_ROOT)
