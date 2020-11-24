from rest_framework import generics

from farmster_server.serializers.crop import CropSerializer
from farmster_server.services import crop as crop_service
#Changes
from farmster_server.models import crop
from django.db.models import Count, Sum


class CropsListCreateApi(generics.ListCreateAPIView):
    queryset = crop_service.get_all_crops()
    serializer_class = CropSerializer
#Changes

    # def get_queryset(self):
    #     return crop.Crop.objects.annotate(
    #         crop_count=Count('name'),
    #         total_sum=Sum('crop_listings__amount')
    #     )


class CropRetrieveUpdateDestroyApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = crop_service.get_all_crops()
    serializer_class = CropSerializer

    # def get_queryset(self):
    #     return crop.Crop.objects.annotate(
    #         crop_count=Count('name'),
    #         total_sum=Sum('crop_listings__amount')
    #     )

crops_list_create = CropsListCreateApi.as_view()
crop_retrieve_update_destroy = CropRetrieveUpdateDestroyApi.as_view()
