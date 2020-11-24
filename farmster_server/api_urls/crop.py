from django.conf.urls import url
from farmster_server.views import crop

crop_urlpatterns = [
    url(r'^crops/$', crop.crops_list_create, name='crops_list_create'),
    url(r'^crops/(?P<pk>\d+)/$', crop.crop_retrieve_update_destroy, name='crop_retrieve_update_destroy')
]
