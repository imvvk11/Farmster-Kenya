from rest_framework import generics
from farmster_server.services import deal as deal_service
from farmster_server.serializers import deal as deal_serializer
from farmster_server.utils.serializer_mixins import UpdateModelWithFullResultMixin, CreateModelWithFullResultMixin


class DealsListCreateApi(CreateModelWithFullResultMixin, generics.ListCreateAPIView):
    queryset = deal_service.get_all_deals()
    write_serializer_class = deal_serializer.DealWriteSerializer
    read_serializer_class = deal_serializer.DealFullSerializer


class DealRetrieveUpdateDestroyApi(UpdateModelWithFullResultMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = deal_service.get_all_deals()
    write_serializer_class = deal_serializer.DealWriteSerializer
    read_serializer_class = deal_serializer.DealFullSerializer


deals_list_create = DealsListCreateApi.as_view()
deal_retrieve_update_destroy = DealRetrieveUpdateDestroyApi.as_view()
