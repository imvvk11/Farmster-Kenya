from datetime import datetime, timedelta
from rest_framework import viewsets
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets

from farmster_server.serializers import crop_listing as crop_listing_serializer
from farmster_server.serializers import place_for_search as place_for_search_serializer
from farmster_server.serializers import search_params as search_params_serializer
from farmster_server.utils.serializer_mixins import CreateModelWithFullResultMixin, UpdateModelWithFullResultMixin
from farmster_server.services import crop_listing as crop_listing_service

from farmster_server.models.crop import Crop
from farmster_server.models.crop_listing import CropListing
from farmster_server.serializers.crop_listing import CropListingCountSerializer
from django.db.models import Sum, Count


class CropsListingListCreateApi(CreateModelWithFullResultMixin, generics.ListCreateAPIView):
    queryset = crop_listing_service.get_all_crop_listings()
    write_serializer_class = crop_listing_serializer.CropListingWriteSerializer
    read_serializer_class = crop_listing_serializer.CropListingFullSerializer


class CropListingRetrieveUpdateDestroyApi(UpdateModelWithFullResultMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = crop_listing_service.get_all_crop_listings()
    write_serializer_class = crop_listing_serializer.CropListingWriteSerializer
    read_serializer_class = crop_listing_serializer.CropListingFullSerializer


class CropListingSearch(generics.ListAPIView):
    serializer_class = place_for_search_serializer.PlaceForSearchSerializer

    def get_queryset(self):
        serializer = search_params_serializer.SearchParamsSerializer(data=self.request.query_params)
        if serializer.is_valid(raise_exception=True):
            queryset = crop_listing_service.search_result(self.request.user.id, **serializer.validated_data)
            return queryset


class FarmersCountFromCropListings(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        serializer = crop_listing_serializer.FarmerByCropListingSerializer(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            listings_count = crop_listing_service.get_farmers_count_by_listings(**serializer.validated_data)
            print('count:', listings_count)
            return Response(status=status.HTTP_202_ACCEPTED, data=listings_count)


class FarmersFromCropListings(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        serializer = crop_listing_serializer.FarmerByCropListingSerializer(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            listings = crop_listing_service.get_farmers_by_listings(**serializer.validated_data)
            return Response(status=status.HTTP_202_ACCEPTED, data=listings)


class CropListingsExpire(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        seven_days_ago = datetime(year=now.year, month=now.month, day=now.day,
                                  tzinfo=timezone.get_current_timezone()) - timedelta(days=7)
        crop_listing_service.expire_crop_listings(seven_days_ago)
        return Response(status=status.HTTP_202_ACCEPTED)


class CropListCountView(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropListingCountSerializer

    def get_queryset(self):
        return Crop.objects.annotate(
            crop_count=Count('id'),
            total_sum=Sum('crop_listings__amount')
        )


crop_listings_expire = CropListingsExpire.as_view()
crop_listing_list_create = CropsListingListCreateApi.as_view()
crop_listing_retrieve_update_destroy = CropListingRetrieveUpdateDestroyApi.as_view()
crop_listing_search = CropListingSearch.as_view()

farmers_from_crop_listings = FarmersFromCropListings.as_view()
farmers_count_from_crop_listings = FarmersCountFromCropListings.as_view()
