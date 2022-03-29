from unicodedata import name
import uuid
from django.db import models


class Parking(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.name


class ParkingSpot(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=50
    )

    parking = models.ForeignKey(
        Parking,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
