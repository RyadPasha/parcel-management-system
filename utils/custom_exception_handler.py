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

from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # Call DRF's default exception handler first to get the standard error response
    response = exception_handler(exc, context)

    if response is not None:
        return Response({
            "success": False,
            "errors": response.data
        }, status=response.status_code)

    # Handle other exceptions - if any
    return Response({
        "success": False,
        "errors": "An unexpected error occurred."
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
