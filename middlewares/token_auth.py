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

from django.http import JsonResponse
from django.conf import settings

class TokenAuthenticationMiddleware:
    """
    Middleware to enforce token-based authentication for API requests.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow unrestricted access to the admin panel
        if request.path.startswith('/admin/'):
            return self.get_response(request)

        # Ensure that settings.SECRET_KEY is not empty
        if not settings.SECRET_KEY:
            return JsonResponse({"detail": "Unauthorized configuration: SECRET_KEY is missing"}, status=500)

        # Extract the token from the Authorization header
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({"detail": "Unauthorized: Token missing or malformed"}, status=401)

        token = auth_header.split(' ')[1]  # Extract the token value
        if token != settings.SECRET_KEY:
            return JsonResponse({"detail": "Unauthorized: Invalid token"}, status=403)

        # Allow the request to proceed if the token is valid
        return self.get_response(request)
