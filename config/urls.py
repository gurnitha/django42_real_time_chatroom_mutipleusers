# config/urls.py

# Django & third parties modules 
from django.contrib import admin
from django.urls import path, include 

# Locals

urlpatterns = [
    
    # personal
    path('', include('app.personal.urls')),

    # admin
    path('admin/', admin.site.urls),
]
