from django.conf.urls import url
from farmster_server.views import farmer

farmer_urlpatterns = [
    url(r'^farmers/$', farmer.farmers_list_create, name='farmers_list_create'),
    url(r'^farmers/(?P<pk>\d+)/$', farmer.farmer_retrieve_update_destroy, name='farmer_retrieve_update_destroy'),
    url(r'^farmers/(?P<farmer_id>\d+)/places/(?P<place_id>\d+)/$', farmer.farmer_places_create_delete,
        name='farmer_places_create_delete'),
    url(r'^farmers/(?P<farmer_id>\d+)/crop-listings/$', farmer.farmer_retrieve_crop_listings,
        name='farmer_retrieve_crop_listing'),
    url(r'^farmers/(?P<farmer_id>\d+)/deals/$', farmer.farmer_retrieve_deals,
        name='farmer_retrieve_deals')

]
