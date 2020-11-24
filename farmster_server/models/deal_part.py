from django.utils import timezone

from django.db import models

from farmster_server.models.crop import Crop
from farmster_server.models.choices import SHIPPING_METHOD, PRICING_TYPE, AMOUNT_UNIT, CROP_QUALITY, CROP_SIZE
from farmster_server.models.deal import Deal


class DealPart(models.Model):
    deal = models.ForeignKey(Deal, on_delete=models.SET_NULL, related_name="deal_parts", null=True)
    crop = models.ForeignKey(Crop, on_delete=models.SET_NULL, related_name="deal_parts", null=True)
    date = models.DateTimeField(default=timezone.now)
    shipping_method = models.CharField(choices=SHIPPING_METHOD.choices,
                                       default=SHIPPING_METHOD.PICKUP, max_length=255, blank=False)
    price = models.FloatField(null=False)
    pricing_type = models.CharField(choices=PRICING_TYPE.choices, default=PRICING_TYPE.PER_KG,
                                    max_length=255, blank=False)
    amount = models.FloatField(null=False)
    amount_unit = models.CharField(choices=AMOUNT_UNIT.choices, default=AMOUNT_UNIT.KGS, max_length=255, blank=False)
    crop_quality = models.CharField(choices=CROP_QUALITY.choices,
                                    default=CROP_QUALITY.UNKNOWN, max_length=255, blank=False)
    crop_size = models.CharField(choices=CROP_SIZE.choices,
                                 default=CROP_SIZE.UNKNOWN, max_length=255, blank=False)
    currency = models.CharField(max_length=3, blank=False)

    def __str__(self):
        return f'{self.crop.name} - {self.amount} {self.amount_unit}'
