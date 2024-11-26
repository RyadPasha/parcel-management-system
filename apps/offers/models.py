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

from django.db import models
from apps.parcels.models import Parcel
from apps.brokers.models import Broker

class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    parcels = models.ManyToManyField(Parcel)
    price_per_meter = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)
