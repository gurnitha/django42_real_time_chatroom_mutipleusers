# app/account/urls.py

# Django & third parties modules 
from django.shortcuts import render
from django.urls import path

# Locals
from app.account import views 

# Create your urls here.

app_name = 'account'

urlpatterns = [
    path('register', views.register_view, name='register'),
]
