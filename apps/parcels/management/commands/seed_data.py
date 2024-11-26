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

from django.core.management.base import BaseCommand
from apps.parcels.models import LandUseGroup, Parcel
from apps.brokers.models import BrokerType
from django.utils.timezone import make_aware
from datetime import datetime

class Command(BaseCommand):
    help = 'Seed initial data into the database'

    def handle(self, *args, **kwargs):
        # Seed LandUseGroup data
        land_use_groups = ['Agricultural', 'Residential', 'Commercial']
        for group in land_use_groups:
            LandUseGroup.objects.get_or_create(name=group)

        # Seed BrokerType data
        broker_types = ['Personal', 'Company', 'Governmental']
        for btype in broker_types:
            BrokerType.objects.get_or_create(name=btype)

        # Seed Parcel data
        parcel_data = [
            (101, 'Al Hamra', 1, 2, 'Residential parcel located in the heart of Riyadh.', '2024-11-01 10:00:00'),
            (102, 'King Abdulaziz Economic City', 2, 3, 'Commercial land near the new economic hub in Jeddah.', '2024-11-02 11:00:00'),
            (103, 'Al Khobar Corniche', 3, 3, 'Prime commercial plot with a stunning view of the Arabian Gulf.', '2024-11-03 12:00:00'),
            (104, 'Abha Hills', 4, 2, 'Residential land surrounded by the scenic mountains of Abha.', '2024-11-04 13:00:00'),
            (105, 'Al Ahsa Oasis', 5, 1, 'Large agricultural parcel in the historic oasis of Al Ahsa.', '2024-11-05 14:00:00'),
            (106, 'Yanbu Industrial Area', 6, 3, 'Commercial land suitable for warehouses and logistics.', '2024-11-06 15:00:00'),
            (107, 'Diriyah', 7, 2, 'Residential plot in the heritage-rich area of Diriyah.', '2024-11-07 16:00:00'),
            (108, 'Qassim Farmland', 8, 1, 'Agricultural land in Qassim known for its date production.', '2024-11-08 17:00:00'),
            (109, 'Jazan Waterfront', 9, 3, 'Commercial land ideal for tourism-related projects.', '2024-11-09 18:00:00'),
            (110, 'Tabuk Greenbelt', 10, 1, 'Agricultural land near the NEOM project.', '2024-11-10 19:00:00'),
        ]

        for block_number, neighbourhood, subdivision_number, land_use_group_id, description, creation_date in parcel_data:
            try:
                land_use_group = LandUseGroup.objects.get(pk=land_use_group_id)
                Parcel.objects.get_or_create(
                    block_number=block_number,
                    neighbourhood=neighbourhood,
                    subdivision_number=subdivision_number,
                    land_use_group=land_use_group,
                    description=description,
                    creation_date=make_aware(datetime.strptime(creation_date, '%Y-%m-%d %H:%M:%S'))
                )

            except LandUseGroup.DoesNotExist:
                self.stderr.write(self.style.ERROR(f"LandUseGroup with id {land_use_group_id} does not exist."))

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
