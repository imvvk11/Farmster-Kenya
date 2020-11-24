from django.conf.urls import url
from farmster_server.views import agent

agent_urlpatterns = [
    url(r'^agents/$', agent.agent_list_create, name='agents_list_create'),
    url(r'^agents/(?P<pk>\d+)/$', agent.agent_retrieve_update_destroy, name='agent_retrieve_update_destroy')
]
