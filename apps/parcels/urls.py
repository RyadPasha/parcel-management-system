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

from django.urls import path
from .views import ParcelListCreateView, ParcelDetailView

urlpatterns = [
    path('', ParcelListCreateView.as_view(), name='parcel-list-create'),
    path('<int:pk>/', ParcelDetailView.as_view(), name='parcel-detail'),
]
