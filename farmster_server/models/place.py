from django.db import models
from farmster_server.managers import place as place_manager
# from django.contrib.gis.db import models


from farmster_server.models.agent import Agent
from farmster_server.models.choices import PLACE_TYPE


class Place(models.Model):
    agents = models.ManyToManyField(Agent, related_name="places", blank=True)
    name = models.CharField(max_length=255, blank=False)
    type = models.CharField(choices=PLACE_TYPE.choices, default=PLACE_TYPE.UNKNOWN, max_length=255, blank=False)
    location_lat = models.FloatField(null=False)
    location_lon = models.FloatField(null=False)
    district = models.CharField(max_length=255, blank=False)
    country = models.CharField(max_length=2, blank=False)
    # point = models.PointField()
    objects = place_manager.PlacesManager()

    def __str__(self):
        return self.name

    class Meta:
        constraints = [models.UniqueConstraint(fields=['name', 'district'], name='unique_name_district'),]
