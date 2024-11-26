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

from time import sleep
from django.core.management.base import BaseCommand
from django.db.models import Count, Q
from apps.parcels.models import Parcel
import requests
from django.conf import settings
from rest_framework import status

class Command(BaseCommand):
    help = 'Monitor parcels and send notifications when all parcels in a block and subdivision have active offers'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Starting parcel monitor..."))
        notified_combinations = set()  # Keep track of notified combinations

        try:
            while True:
                # Query parcels grouped by block and subdivision
                parcels_with_active_offers = (
                    Parcel.objects.values('block_number', 'subdivision_number')
                    .annotate(
                        active_count=Count('id', filter=Q(offer__isnull=False)),
                        total_count=Count('id')
                    )
                )

                # Check for fully active parcels and trigger notifications
                for group in parcels_with_active_offers:

                    if group['active_count'] == group['total_count']:
                        combination_key = (group['block_number'], group['subdivision_number'])

                        # Skip if already notified
                        if combination_key in notified_combinations:
                            continue

                        try:
                            # Send notification to dummy API
                            response = requests.post(
                                settings.NOTIFICATION_SERVICE_API_URL,
                                json={
                                    "block_number": group['block_number'],
                                    "subdivision_number": group['subdivision_number']
                                },
                                timeout=5  # Set a timeout for the request
                            )

                            if response.status_code == status.HTTP_200_OK:
                                self.stdout.write(self.style.SUCCESS(
                                    f"Notification sent for Block {group['block_number']} "
                                    f"Subdivision {group['subdivision_number']}"
                                ))
                                notified_combinations.add(combination_key)
                            else:
                                self.stdout.write(self.style.ERROR(
                                    f"Failed to send notification: {response.status_code}"
                                ))
                        except requests.RequestException as e:
                            self.stderr.write(f"Error sending notification: {e}")

                # Run every 60 seconds
                sleep(60)

        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("Stopping parcel monitor..."))
