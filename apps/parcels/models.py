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
from django.utils.timezone import now

class LandUseGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Parcel(models.Model):
    block_number = models.IntegerField()
    neighbourhood = models.TextField()
    subdivision_number = models.IntegerField()
    land_use_group = models.ForeignKey(LandUseGroup, on_delete=models.CASCADE)
    description = models.TextField()
    creation_date = models.DateTimeField(default=now)
