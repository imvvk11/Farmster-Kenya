from django.conf.urls import url
from farmster_server.views import user_crops

user_crops_urlpatterns = [
    url(r'^users/(?P<user_id>\d+)/crops/$', user_crops.user_crops_list_create, name='user_crops_list_create'),
    url(r'^users/(?P<user_id>\d+)/crops/(?P<crop_id>\d+)/$', user_crops.user_crops_destroy, name='user_crops_destroy')
]
