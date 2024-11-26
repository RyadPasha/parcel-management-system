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

from rest_framework.response import Response
from rest_framework import generics, filters, status
from .models import Broker, BrokerType
from .serializers import BrokerSerializer, BrokerTypeSerializer
from django_filters.rest_framework import DjangoFilterBackend

class BrokerListCreateView(generics.ListCreateAPIView):
    queryset = Broker.objects.all()
    serializer_class = BrokerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['type', 'creation_date']  # Add fields to filter by (?field=<value>)
    search_fields = ['name', 'email', 'phone_number']  # Add search fields (?search=<query>)
    ordering_fields = ['creation_date', 'last_update_date']  # Add fields to sort by (?ordering=<field>)
    ordering = ['creation_date']  # Default ordering

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"id": response.data["id"], "success": True},
            status=status.HTTP_201_CREATED
        )

class BrokerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Broker.objects.all()
    serializer_class = BrokerSerializer

class BrokerTypeListView(generics.ListAPIView):
    queryset = BrokerType.objects.all()
    serializer_class = BrokerTypeSerializer
