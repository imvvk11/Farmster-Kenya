from django.conf.urls import url
from farmster_server.views import deal

deal_urlpatterns = [
    url(r'^deals/$', deal.deals_list_create, name='deals_list_create'),
    url(r'^deals/(?P<pk>\d+)/$', deal.deal_retrieve_update_destroy, name='deal_retrieve_update_destroy')
]
