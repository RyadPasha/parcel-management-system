"""
======================================================================
Project Name: Parcel Offers Management System
Description:
    A backend API project for managing offers on predefined parcels
    of land. This project includes features for handling brokers,
    parcels, and offers, along with background jobs for monitoring
    and notification.

Author: Mohamed Riyad
Email: mohamed@ryad.dev
Website: https://ryad.dev

License: MIT License
======================================================================
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/parcels/', include('apps.parcels.urls')),
    path('api/brokers/', include('apps.brokers.urls')),
    path('api/offers/', include('apps.offers.urls')),
]
