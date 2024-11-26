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
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import generics, filters, status
from django_filters import NumberFilter
from .models import Offer
from .serializers import OfferSerializer

class OfferFilter(FilterSet):
    price_per_meter_min = NumberFilter(field_name="price_per_meter", lookup_expr="gte")  # Minimum price filter
    price_per_meter_max = NumberFilter(field_name="price_per_meter", lookup_expr="lte")  # Maximum price filter

    class Meta:
        model = Offer
        fields = ['broker', 'creation_date']  # Other filterable fields

class OfferListCreateView(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = OfferFilter  # Use the custom filter class (?price_per_meter_min=<value>&price_per_meter_max=<value>)
    search_fields = ['title', 'description']  # Add search fields (?search=<query>)
    ordering_fields = ['creation_date', 'last_update_date', 'price_per_meter']  # Add fields to sort by (?ordering=<field>)
    ordering = ['creation_date']  # Default ordering

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"id": response.data["id"], "success": True}, status=status.HTTP_201_CREATED)

class OfferDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class OfferUpdateView(generics.UpdateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({
            "success": True,
            "message": "Offer updated successfully!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

class OfferDeleteView(generics.DestroyAPIView):
    queryset = Offer.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({
            "success": True,
            "message": "Offer deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)