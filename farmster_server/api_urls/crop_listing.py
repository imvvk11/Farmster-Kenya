from django.urls import path, include
from django.conf.urls import url
from farmster_server.views import crop_listing
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("crop-listing/crops/count", crop_listing.CropListCountView, basename="CropListCountView")

crop_listing_urlpatterns = [
    path('', include(router.urls)),
    url(r'^crop-listings/$', crop_listing.crop_listing_list_create, name='crops_listing_list_create'),
    url(r'^crop-listings/expire/$', crop_listing.crop_listings_expire, name='crop_listings_expire'),
    url(r'^crop-listings/(?P<pk>\d+)/$', crop_listing.crop_listing_retrieve_update_destroy,
        name='crop_listing_retrieve_update_destroy'),
    url(r'^crop-listings/places/search/$', crop_listing.crop_listing_search,
        name='crop_listing_search'),
    url(r'^crop-listings/farmers/$', crop_listing.farmers_from_crop_listings),
    url(r'^crop-listings/farmers/count/$', crop_listing.farmers_count_from_crop_listings),
]
