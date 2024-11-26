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
from .models import Offer
from apps.parcels.models import Parcel, LandUseGroup
from apps.brokers.models import Broker, BrokerType

class OfferModelTest(TestCase):
    def setUp(self):
        self.land_use_group = LandUseGroup.objects.create(name="Commercial")
        self.parcel = Parcel.objects.create(
            block_number=1,
            neighbourhood="Al Khobar Corniche",
            subdivision_number=101,
            land_use_group=self.land_use_group,
            description="Commercial parcel near the Al Khobar Corniche"
        )
        self.broker_type = BrokerType.objects.create(name="Company")
        self.broker = Broker.objects.create(
            name="Saudi Realty Co.",
            type=self.broker_type,
            phone_number="+966531234567",
            email="info@saudirealty.sa",
            address="Prince Sultan Road, Jeddah",
            bio="Leading real estate broker in Jeddah"
        )
        self.offer = Offer.objects.create(
            title="Prime Commercial Property",
            description="Ideal for retail",
            broker=self.broker,
            price_per_meter=500.00
        )
        self.offer.parcels.add(self.parcel)

    def test_offer_creation(self):
        self.assertEqual(self.offer.title, "Prime Commercial Property")
        self.assertEqual(self.offer.broker.name, "Saudi Realty Co.")

class OfferAPITest(TestCase):
    def setUp(self):
        self.land_use_group = LandUseGroup.objects.create(name="Commercial")
        self.parcel = Parcel.objects.create(
            block_number=1,
            neighbourhood="Al Khobar Corniche",
            subdivision_number=101,
            land_use_group=self.land_use_group,
            description="Commercial parcel near the Al Khobar Corniche"
        )
        self.broker_type = BrokerType.objects.create(name="Company")
        self.broker = Broker.objects.create(
            name="Saudi Realty Co.",
            type=self.broker_type,
            phone_number="+966531234567",
            email="info@saudirealty.sa",
            address="Prince Sultan Road, Jeddah",
            bio="Leading real estate broker in Jeddah"
        )
        self.auth_header = {"HTTP_AUTHORIZATION": f"Bearer {settings.SECRET_KEY}"}

    def test_offer_list_api_with_auth(self):
        response = self.client.get("/api/offers/", **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_offer_api_with_auth(self):
        response = self.client.post(
            "/api/offers/",
            data={
                "title": "New Offer",
                "description": "A great deal",
                "broker": self.broker.id,
                "parcels": [self.parcel.id],
                "price_per_meter": 300.00
            },
            **self.auth_header
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_offer_list_api_without_auth(self):
        response = self.client.get("/api/offers/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
