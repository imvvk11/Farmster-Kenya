from django.conf.urls import url
from farmster_server.views import contact

contact_urlpatterns = [
    url(r'^contacts/$', contact.contacts_list_create, name='contacts_list_create'),
    url(r'^contacts/(?P<pk>\d+)/$', contact.contact_retrieve_update_destroy, name='contact_retrieve_update_destroy')
]
