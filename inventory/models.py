from django.db import models

INVENTORY_STATUS = [
    ('available', 'Available'),
    ('sold', 'Sold'),
    ('delisted', 'Delisted'),
]


class Car(models.Model):
    status = models.CharField(choices=INVENTORY_STATUS, max_length=9)
    year = models.CharField(max_length=6, blank=True)
    make = models.CharField(max_length=30, blank=True)
    model = models.CharField(max_length=30, blank=True)
    vin = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=30, blank=True)
    mileage = models.CharField(max_length=9, blank=True)
    price = models.CharField(max_length=30, blank=True)
    description = models.TextField()  # rendered markup (client requirement)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']
