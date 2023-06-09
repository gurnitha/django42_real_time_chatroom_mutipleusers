# config/urls.py

# Django & third parties modules 
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include 

# Locals
# from app.personal.views import (
#     home_screen_view
# )

urlpatterns = [
    
    # account
    path('', include('app.account.urls', namespace='account')),
    
    # personal
    path('', include('app.personal.urls', namespace='personal')),

    # admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


