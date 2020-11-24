from django.db import models
from django.db.models import QuerySet


class DealManager(models.Manager):

    def get_all_deals_by_farmer_id(self, farmer_id: int) -> models.QuerySet:
        return self.filter(farmer_id=farmer_id).prefetch_related('farmer', 'farmer__places', 'farmer__places__agents')


