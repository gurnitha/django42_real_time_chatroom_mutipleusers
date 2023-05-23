# app/personal/views.py

# Django & third parties modules 
from django.shortcuts import render

# Locals

# Create your views here.

def home_screen_view(request, *args, **kwargs):
	context = {}
	return render(request, 'personal/home.html', context)