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
from .views import BrokerListCreateView, BrokerDetailView, BrokerTypeListView

urlpatterns = [
    path('', BrokerListCreateView.as_view(), name='broker-list-create'), # Add a new broker
    path('<int:pk>/', BrokerDetailView.as_view(), name='broker-detail'), # Get a broker by ID
    path('types/', BrokerTypeListView.as_view(), name='broker-type-list'), # Get all brokers
]
