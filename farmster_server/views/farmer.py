from rest_framework import generics, status
from rest_framework.response import Response
from farmster_server.serializers import farmer as farmer_serializer
from farmster_server.serializers.crop_listing import CropListingFullSerializer
from farmster_server.serializers.deal import DealFullSerializer
from farmster_server.serializers.place import PlaceFullSerializer
from farmster_server.services import farmer as farmer_service
from farmster_server.services import crop_listing as crop_listing_service
from farmster_server.services import deal as deal_service
from farmster_server.utils.serializer_mixins import CreateModelWithFullResultMixin, UpdateModelWithFullResultMixin


class FarmerListCreateApi(CreateModelWithFullResultMixin, generics.ListCreateAPIView):
    queryset = farmer_service.get_all_farmers()
    write_serializer_class = farmer_serializer.FarmerWriteSerializer
    read_serializer_class = farmer_serializer.FarmerFullSerializer


class FarmerRetrieveUpdateDestroyApi(UpdateModelWithFullResultMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = farmer_service.get_all_farmers()
    write_serializer_class = farmer_serializer.FarmerWriteSerializer
    read_serializer_class = farmer_serializer.FarmerFullSerializer


class FarmerPlacesCreateDeleteApi(generics.GenericAPIView):
    serializer_class = PlaceFullSerializer

    def get_queryset(self):
        farmer_id = self.kwargs['farmer_id']
        queryset = farmer_service.get_farmer_by_id(farmer_id)
        return queryset

    def post(self, request, *args, **kwargs):
        farmer_id = kwargs['farmer_id']
        place_id = kwargs['place_id']
        farmer = farmer_service.add_place_for_farmer(farmer_id, place_id)
        serializer_class = self.get_serializer_class()
        return Response(data=serializer_class(farmer.places, many=True).data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        farmer_id = kwargs['farmer_id']
        place_id = kwargs['place_id']
        farmer_service.remove_place_from_farmer(farmer_id, place_id)
        # The valid status is 204, changed to solve client error
        return Response(status=status.HTTP_200_OK)


class FarmerRetrieveCropListings(generics.ListAPIView):
    serializer_class = CropListingFullSerializer

    def get_queryset(self):
        queryset = crop_listing_service.get_all_active_crop_listings_by_farmer_id(self.kwargs['farmer_id'])
        return queryset


class FarmerRetrieveDeals(generics.ListAPIView):
    serializer_class = DealFullSerializer

    def get_queryset(self):
        queryset = deal_service.get_all_crop_listings_by_farmer_id(self.kwargs['farmer_id'])
        return queryset


farmers_list_create = FarmerListCreateApi.as_view()
farmer_retrieve_update_destroy = FarmerRetrieveUpdateDestroyApi.as_view()
farmer_places_create_delete = FarmerPlacesCreateDeleteApi.as_view()
farmer_retrieve_crop_listings = FarmerRetrieveCropListings.as_view()
farmer_retrieve_deals = FarmerRetrieveDeals.as_view()

