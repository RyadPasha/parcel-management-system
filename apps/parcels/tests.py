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

from django.test import TestCase
from django.conf import settings
from rest_framework import status
from .models import Parcel, LandUseGroup

class ParcelModelTest(TestCase):
    def setUp(self):
        self.land_use_group = LandUseGroup.objects.create(name="Residential")
        self.parcel = Parcel.objects.create(
            block_number=1,
            neighbourhood="Al Olaya",
            subdivision_number=101,
            land_use_group=self.land_use_group,
            description="A parcel of land in Riyadh",
        )

    def test_parcel_creation(self):
        self.assertEqual(self.parcel.block_number, 1)
        self.assertEqual(self.parcel.land_use_group.name, "Residential")
        self.assertEqual(str(self.parcel), f"Parcel object ({self.parcel.id})")

    def test_land_use_group_creation(self):
        self.assertEqual(self.land_use_group.name, "Residential")

class ParcelAPITest(TestCase):
    def setUp(self):
        # Create a land use group for testing, to be used in the Parcel creation
        self.land_use_group = LandUseGroup.objects.create(name="Residential")
        self.auth_header = {"HTTP_AUTHORIZATION": f"Bearer {settings.SECRET_KEY}"}

    def test_parcel_list_api(self):
        response = self.client.get("/api/parcels/", **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_parcel_api(self):
        response = self.client.post(
            "/api/parcels/",
            data={
                "block_number": 202,
                "neighbourhood": "Al Malaz",
                "subdivision_number": 3,
                "land_use_group": self.land_use_group.id,
                "description": "A residential parcel in Al Malaz, Riyadh, ideal for housing development."
            },
            **self.auth_header
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_parcel_list_api_without_auth(self):
        response = self.client.get("/api/parcels/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
