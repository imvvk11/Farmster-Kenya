from django.conf.urls import url
from farmster_server.views import user_places

user_places_urlpatterns = [
    url(r'^users/(?P<user_id>\d+)/places/$', user_places.user_places_list_create, name='user_places_list_create'),
    url(r'^users/(?P<user_id>\d+)/places/(?P<place_id>\d+)/$', user_places.user_places_destroy,
        name='user_places_destroy')
]
