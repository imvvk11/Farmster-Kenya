from django.db import models

from farmster_server.models.choices import CROP_TYPE


class Crop(models.Model):
    name = models.CharField(max_length=255, blank=False)
    image_url = models.URLField(max_length=255, blank=True)
    type = models.CharField(choices=CROP_TYPE.choices, default=CROP_TYPE.UNKNOWN, max_length=255, blank=False)

    def __str__(self):
        return self.name
