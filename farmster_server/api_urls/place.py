from django.conf.urls import url
from farmster_server.views import place

place_urlpatterns = [
    url(r'^places/$', place.places_list_create, name='places_list_create'),
    url(r'^places/(?P<pk>\d+)/$', place.places_retrieve_update_destroy, name='places_retrieve_update_destroy'),
    url(r'^places/(?P<place_id>\d+)/agents/(?P<agent_id>\d+)/$', place.place_agents_create_delete,
        name='place_agents_create_delete'),
    url(r'^places/(?P<place_id>\d+)/crop-listings/$', place.place_retrieve_crop_listing,
        name='place_retrieve_crop_listing'),
    url(r'^places/search/$', place.place_search, name='place_search'),
    url(r'^places/regions/$', place.places_get_regions, name='get_regions')
]
