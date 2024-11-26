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
from .views import OfferListCreateView, OfferDetailView, OfferUpdateView, OfferDeleteView

urlpatterns = [
    path('', OfferListCreateView.as_view(), name='offer-list-create'),
    path('<int:pk>/', OfferDetailView.as_view(), name='offer-detail'),
    path('<int:pk>/update/', OfferUpdateView.as_view(), name='offer-update'),
    path('<int:pk>/delete/', OfferDeleteView.as_view(), name='offer-delete'),
]
