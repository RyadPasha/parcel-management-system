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

class BrokerType(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Broker(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(BrokerType, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    bio = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)
