# app/personal/views.py

# Django & third parties modules 
from django.shortcuts import render

# Locals

# Create your views here.

def home_page(request):
	return render(request, 'app/personal/index.html')