from rest_framework.response import Response
from rest_framework import generics, status

from farmster_server.serializers import place as place_serializer
from farmster_server.serializers.agent import AgentSerializer
from farmster_server.serializers.crop_listing import CropListingFullSerializer
from farmster_server.serializers.place_search_params import PlaceSearchParamsSerializer, FavoriteOnlyParamsSerializer
from farmster_server.services import place as place_service
from farmster_server.services import crop_listing as crop_listing_service
from farmster_server.utils.serializer_mixins import CreateModelWithFullResultMixin, UpdateModelWithFullResultMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class PlacesListCreateApi(CreateModelWithFullResultMixin, generics.ListCreateAPIView):
    queryset = place_service.get_all_places()
    write_serializer_class = place_serializer.PlaceWriteSerializer
    read_serializer_class = place_serializer.PlaceFullSerializer


class PlacesRetrieveUpdateDestroyAPI(UpdateModelWithFullResultMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = place_service.get_all_places()
    write_serializer_class = place_serializer.PlaceWriteSerializer
    read_serializer_class = place_serializer.PlaceFullSerializer


class PlaceAgentsCreateDeleteApi(generics.GenericAPIView):
    serializer_class = AgentSerializer

    def get_queryset(self):
        place_id = self.kwargs['place_id']
        queryset = place_service.get_place_by_id(place_id)
        return queryset

    def post(self, request, *args, **kwargs):
        place_id = kwargs['place_id']
        agent_id = kwargs['agent_id']
        place = place_service.add_agent_for_place(place_id, agent_id)
        serializer_class = self.get_serializer_class()
        return Response(data=serializer_class(place.agents, many=True).data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        place_id = kwargs['place_id']
        agent_id = kwargs['agent_id']
        place_service.remove_agent_from_place(place_id, agent_id)
        # The valid status is 204, changed to solve client error
        return Response(status=status.HTTP_200_OK)


class PlacesRetrieveAllRegions(generics.GenericAPIView):
    # DELETE ME!!!
    from rest_framework.permissions import AllowAny
    permission_classes = (AllowAny,)
    # TO here

    # 2 hour cache - global
    @method_decorator(cache_page(60*60*2))
    def get(self, request, *args, **kwargs):
        regions = place_service.get_all_regions()
        return Response(status=status.HTTP_202_ACCEPTED, data=regions)


class PlaceRetrieveCropListing(generics.ListAPIView):
    serializer_class = CropListingFullSerializer

    def get_queryset(self):
        farmers = place_service.get_all_farmer_by_place_id(self.kwargs['place_id'])
        farmer_ids = [farmer.id for farmer in farmers]
        serializer = FavoriteOnlyParamsSerializer(data=self.request.query_params)
        favorite_crops_only = False
        if serializer.is_valid():
            favorite_crops_only = serializer.validated_data['favorite_crops_only']
        queryset = crop_listing_service\
            .get_all_active_crop_listings_by_farmer_ids(self.request.user.id, farmer_ids, favorite_crops_only)
        return queryset


class PlaceSearch(generics.ListAPIView):
    serializer_class = place_serializer.PlaceWithDistanceSerializer

    def get_queryset(self):
        serializer = PlaceSearchParamsSerializer(data=self.request.query_params)
        if serializer.is_valid(raise_exception=True):
            queryset = place_service.get_places_by_name_or_district(**serializer.validated_data)
            return queryset


places_get_regions = PlacesRetrieveAllRegions.as_view()
places_list_create = PlacesListCreateApi.as_view()
places_retrieve_update_destroy = PlacesRetrieveUpdateDestroyAPI.as_view()
place_agents_create_delete = PlaceAgentsCreateDeleteApi.as_view()
place_retrieve_crop_listing = PlaceRetrieveCropListing.as_view()
place_search = PlaceSearch.as_view()
