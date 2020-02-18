from django.db import models

INVENTORY_STATUS = [
    ('available', 'Available'),
    ('sold', 'Sold'),
    ('delete', 'Delisted'),
]


class Item(models.Model):
    inventoryid = models.CharField(max_length=30, blank=True)
    year = models.CharField(max_length=30)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=150)
    vin = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=30, blank=True)
    mileage = models.CharField(max_length=30, blank=True)
    price = models.CharField(max_length=30, blank=True)
    description = models.TextField()  # rendered markup (client requirement)
    status = models.CharField(choices=INVENTORY_STATUS, max_length=9)
    thumbnail = models.CharField(max_length=300, blank=True)
    path = models.CharField(max_length=300, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']
