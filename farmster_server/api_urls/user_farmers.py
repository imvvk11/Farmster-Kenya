from django.conf.urls import url
from farmster_server.views import user_farmers

user_farmers_urlpatterns = [
    url(r'^users/(?P<user_id>\d+)/farmers/$',
        user_farmers.user_farmer_list_create, name='user_farmer_list_create'),
    url(r'^users/(?P<user_id>\d+)/farmers/(?P<farmer_id>\d+)/$',
        user_farmers.user_farmer_destroy, name='user_farmer_destroy')
]
