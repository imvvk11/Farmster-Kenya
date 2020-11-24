from django.db import models
from farmster_server.managers import crop_listing as crop_listing_manager
from farmster_server.models.choices import AMOUNT_UNIT, CROP_LISTING_STATUS
from farmster_server.models.crop import Crop
from farmster_server.models.farmer import Farmer
from django.utils import timezone


class CropListing(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name="crop_listings")
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name="crop_listings")
    harvest_date = models.DateTimeField(default=timezone.now)
    variety = models.CharField(max_length=255, blank=True)
    amount = models.FloatField(null=False)
    amount_unit = models.CharField(choices=AMOUNT_UNIT.choices, default=AMOUNT_UNIT.KGS,
                                   max_length=255, blank=False)
    status = models.CharField(choices=CROP_LISTING_STATUS.choices, default=CROP_LISTING_STATUS.ACTIVE,
                              max_length=255, blank=False)


    objects = crop_listing_manager.CropListingManager()

    class Meta:
        ordering = ('harvest_date',)

    def __str__(self):
        if self.crop:
            return self.crop.name
        return 'No Crop'
