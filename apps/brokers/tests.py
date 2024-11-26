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
from .models import Broker, BrokerType

class BrokerModelTest(TestCase):
    def setUp(self):
        self.broker_type = BrokerType.objects.create(name="Personal")
        self.broker = Broker.objects.create(
            name="Ahmed Al-Qahtani",
            type=self.broker_type,
            phone_number="+966501234567",
            email="ahmed.alqahtani@gmail.com",
            address="King Abdullah Road, Riyadh",
            bio="Experienced real estate broker in Saudi Arabia"
        )

    def test_broker_creation(self):
        self.assertEqual(self.broker.name, "Ahmed Al-Qahtani")
        self.assertEqual(self.broker.type.name, "Personal")

    def test_broker_type_creation(self):
        self.assertEqual(self.broker_type.name, "Personal")

class BrokerAPITest(TestCase):
    def setUp(self):
        self.broker_type = BrokerType.objects.create(name="Personal")
        self.auth_header = {"HTTP_AUTHORIZATION": f"Bearer {settings.SECRET_KEY}"}

    def test_broker_list_api(self):
        response = self.client.get("/api/brokers/", **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_broker_api(self):
        response = self.client.post(
            "/api/brokers/",
            data={
                "name": "Ahmed Al-Qahtani",
                "type": self.broker_type.id,
                "phone_number": "+966501234567",
                "email": "ahmed.alqahtani@gmail.com",
                "address": "King Abdullah Road, Riyadh",
                "bio": "New broker"
            },
            **self.auth_header
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_broker_list_api_without_auth(self):
        response = self.client.get("/api/brokers/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
