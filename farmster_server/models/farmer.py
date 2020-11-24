from django.db import models

from farmster_server.models.place import Place
from farmster_server.managers import farmer as farmer_manager


class Farmer(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=True, default='')
    phone_number = models.CharField(max_length=255, blank=False, unique=True)
    places = models.ManyToManyField(Place, related_name="farmers")

    objects = farmer_manager.FarmerManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

