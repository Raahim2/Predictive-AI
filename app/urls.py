from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path("", views.index , name="home"),
    path("HPP", views.HPP , name="predict"),
    path("CR", views.CR , name="clg"),
    path("FPP", views.FPP , name="FPP"),
    path("HDC", views.HDC , name="HDC"),
    path("PDC", views.PDC , name="PDC"),




    
]