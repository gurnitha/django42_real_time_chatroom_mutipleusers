# app/personal/urls.py

# Django & third parties modules 
from django.shortcuts import render
from django.urls import path

# Locals
from app.personal import views 

# Create your urls here.

app_name = 'personal'

urlpatterns = [
    path('', views.home_screen_view, name='home'),
]
