from django.db import models
from django.db.models import QuerySet

from farmster_server.models.choices import CROP_LISTING_STATUS


class CropListingManager(models.Manager):

    def get_all_active_crop_listings(self) -> models.QuerySet:
        return self.filter(status=CROP_LISTING_STATUS.ACTIVE).prefetch_related(
            'farmer', 'farmer__places', 'farmer__places__agents')

    def filter_crop_listing_by_region_id(self, query: QuerySet, regions: [int]) -> QuerySet:
        # TODO - complete
        return query
        # return query.filter(region__in=regions)

    def get_all_active_crop_listings_by_farmer_id(self, farmer_id: int) -> models.QuerySet:
        return self.filter(status=CROP_LISTING_STATUS.ACTIVE,
                           farmer_id=farmer_id).prefetch_related('farmer', 'farmer__places', 'farmer__places__agents')

    def get_all_active_crop_listings_by_farmer_ids(self, farmer_ids: [int]) -> models.QuerySet:
        return self.filter(status=CROP_LISTING_STATUS.ACTIVE, farmer_id__in=farmer_ids).prefetch_related(
            'farmer', 'farmer__places', 'farmer__places__agents')

    def filter_crop_listing_by_crops_id(self, query: QuerySet, crop_ids: [int]) -> QuerySet:
        return query.filter(crop__in=crop_ids)

    def filter_crop_listing_by_user_favorite_place(self, query: QuerySet, user_favorite_places: [int]) -> QuerySet:
        return query.filter(farmer__places__in=user_favorite_places)

    def filter_crop_listing_by_user_favorite_farmers(self, query: QuerySet, user_favorite_farmers: [int]) -> QuerySet:
        return query.filter(farmer__in=user_favorite_farmers)

    def filter_crop_listing_by_queryset_harvest_time_from(self, query: QuerySet, harvest_time_from) -> QuerySet:
        return query.filter(harvest_date__gte=harvest_time_from)

    def filter_crop_listing_by_queryset_harvest_time_to(self, query: QuerySet, harvest_time_to) -> QuerySet:
        return query.filter(harvest_date__lte=harvest_time_to)

    def filter_crop_listing_by_status(self, query: QuerySet, status: CROP_LISTING_STATUS) -> QuerySet:
        return query.filter(status=status)

    def filter_crop_listing_by_queryset_district(self, query: QuerySet, district_names: [str]) -> QuerySet:
        return query.filter(farmer__places__district__in=district_names)