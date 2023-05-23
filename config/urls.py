# config/urls.py

# Django & third parties modules 
from django.contrib import admin
from django.urls import path, include 

# Locals
from app.personal.views import (
    home_screen_view
)

urlpatterns = [
    
    # personal
    path('', home_screen_view, name='home'),

    # admin
    path('admin/', admin.site.urls),
]
