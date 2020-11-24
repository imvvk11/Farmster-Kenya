import sys
from datetime import datetime

import geopy.distance
from django.db.models import QuerySet
from functools import cmp_to_key

from farmster_server.models.choices import CROP_LISTING_STATUS
from farmster_server.models.crop_listing import CropListing
from farmster_server.services import user as user_service


def get_all_active_crop_listings() -> QuerySet:
    return CropListing.objects.get_all_active_crop_listings()


def get_all_crop_listings() -> QuerySet:
    return CropListing.objects.all()


def get_crop_listing_by_id(crop_listing: int) -> QuerySet:
    return CropListing.objects.get(id=crop_listing)


def get_all_active_crop_listings_by_farmer_id(farmer_id: int) -> QuerySet:
    return CropListing.objects.get_all_active_crop_listings_by_farmer_id(farmer_id)


def get_all_active_crop_listings_by_farmer_ids(user_id: int, farmer_ids: [int], favorite_crops_only: bool = False) -> QuerySet:
    queryset = CropListing.objects.get_all_active_crop_listings_by_farmer_ids(farmer_ids)
    if favorite_crops_only:
        user_favorite_crops = [crop.id for crop in user_service.get_user_crops(user_id)]
        queryset = CropListing.objects.filter_crop_listing_by_crops_id(queryset, user_favorite_crops)
    return queryset


def get_farmers_by_listings(crops: [int] = [], harvest_time_to = None, harvest_time_from = None, regions = []) -> []:
    queryset = get_all_crop_listings()
    if crops:
        queryset = CropListing.objects.filter_crop_listing_by_crops_id(queryset, crops)
    if harvest_time_from:
        queryset = CropListing.objects.filter_crop_listing_by_queryset_harvest_time_from(queryset, harvest_time_from)
    if harvest_time_to:
        queryset = CropListing.objects.filter_crop_listing_by_queryset_harvest_time_to(queryset, harvest_time_to)
    if regions:
        queryset = CropListing.objects.filter_crop_listing_by_queryset_district(queryset, regions)
    phone_numbers = list()
    for crop_listing in queryset:
        phone_numbers.append(crop_listing.farmer.phone_number)
    return phone_numbers


def get_farmers_count_by_listings(crops: [int] = [], harvest_time_to = None, harvest_time_from = None, regions = []) -> []:
    queryset = get_all_crop_listings()
    if crops:
        queryset = CropListing.objects.filter_crop_listing_by_crops_id(queryset, crops)
    if harvest_time_from:
        queryset = CropListing.objects.filter_crop_listing_by_queryset_harvest_time_from(queryset, harvest_time_from)
    if harvest_time_to:
        queryset = CropListing.objects.filter_crop_listing_by_queryset_harvest_time_to(queryset, harvest_time_to)
    if regions:
        queryset = CropListing.objects.filter_crop_listing_by_queryset_district(queryset, regions)
    return queryset.count()



def search_result(user_id: int, user_lat: float, user_lon: float, favorite_crops_only: bool = None,
                  favorite_farmer_only: bool = None, favorite_places_only: bool = None,
                  min_distance_km: float = None, max_distance_km: float = None,
                  harvest_time_from: int = None, harvest_time_to: int = None, crops: [int] = []) -> []:
    queryset = get_all_active_crop_listings()
    user_favorite_places_ids = []
    if favorite_crops_only:
        user_favorite_crops = [crop.id for crop in user_service.get_user_crops(user_id)]
        queryset = CropListing.objects.filter_crop_listing_by_crops_id(queryset, user_favorite_crops)
    if crops:
        queryset = CropListing.objects.filter_crop_listing_by_crops_id(queryset, crops)
    if favorite_places_only:
        user_favorite_places_ids = [place.id for place in user_service.get_user_places(user_id)]
        queryset = CropListing.objects.filter_crop_listing_by_user_favorite_place(queryset, user_favorite_places_ids)
    if favorite_farmer_only:
        user_favorite_farmers_ids = [farmer.id for farmer in user_service.get_user_farmers(user_id)]
        queryset = CropListing.objects.filter_crop_listing_by_user_favorite_place(queryset, user_favorite_farmers_ids)
    if harvest_time_from:
        queryset = CropListing.objects.filter_crop_listing_by_queryset_harvest_time_from(queryset, harvest_time_from)
    if harvest_time_to:
        queryset = CropListing.objects.filter_crop_listing_by_queryset_harvest_time_to(queryset, harvest_time_to)

    place_dict = {}
    for crop_listing in queryset:
        curr_places = crop_listing.farmer.places.all()
        for place in curr_places:
            if place not in place_dict:
                place_dict[place] = list()

            place_dict[place].append(crop_listing)

    places = list()
    for place, crop_listings in place_dict.items():
        if favorite_places_only and place.id not in user_favorite_places_ids:
            continue

        coords_1 = (user_lat, user_lon)
        coords_2 = (place.location_lat, place.location_lon)
        distance = geopy.distance.vincenty(coords_1, coords_2).km
        place.crops_listings_count = len(crop_listings)
        place.distance_km = distance
        places.append(place)

    if min_distance_km or max_distance_km:
        if not min_distance_km:
            min_distance_km = 0
        if not max_distance_km:
            max_distance_km = sys.float_info.max

        filtered_places = list()
        for place in places:
            if max_distance_km >= place.distance_km >= min_distance_km:
                filtered_places.append(place)

        places = filtered_places

    sorted(places, key=cmp_to_key(lambda place1, place2: place1.distance_km - place2.distance_km))
    return places


def expire_crop_listings(since: datetime):
    queryset = CropListing.objects.all()
    queryset = CropListing.objects.filter_crop_listing_by_queryset_harvest_time_to(queryset, since)
    queryset = CropListing.objects.filter_crop_listing_by_status(queryset, CROP_LISTING_STATUS.ACTIVE)
    queryset.update(status=CROP_LISTING_STATUS.EXPIRED)
