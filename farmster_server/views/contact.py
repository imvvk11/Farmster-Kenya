from rest_framework import generics
from farmster_server.services import contact as contact_service
from farmster_server.serializers import contact as contact_serializer


class ContactsListCreateApi(generics.ListCreateAPIView):
    queryset = contact_service.get_all_contacts()
    serializer_class = contact_serializer.ContactSerializer


class ContactRetrieveUpdateDestroyApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = contact_service.get_all_contacts()
    serializer_class = contact_serializer.ContactSerializer


contacts_list_create = ContactsListCreateApi.as_view()
contact_retrieve_update_destroy = ContactRetrieveUpdateDestroyApi.as_view()
