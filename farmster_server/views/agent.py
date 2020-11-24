from rest_framework import generics

from farmster_server.serializers.agent import AgentSerializer
from farmster_server.services import agent as agent_service


class AgentListCreateApi(generics.ListCreateAPIView):
    queryset = agent_service.get_all_agents()
    serializer_class = AgentSerializer


class AgentRetrieveUpdateDestroyApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = agent_service.get_all_agents()
    serializer_class = AgentSerializer


agent_list_create = AgentListCreateApi.as_view()
agent_retrieve_update_destroy = AgentRetrieveUpdateDestroyApi.as_view()
