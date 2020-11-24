from django.conf.urls import url
from farmster_server.views import user_crop_listings

user_crop_listings_urlpatterns = [
    url(r'^users/(?P<user_id>\d+)/crop-listings/$',
        user_crop_listings.user_crop_listings_list_create, name='user_crop_listings_list_create'),
    url(r'^users/(?P<user_id>\d+)/crop-listings/(?P<crop_listing_id>\d+)/$',
        user_crop_listings.user_crop_listings_destroy, name='user_crop_listings_destroy')
]
