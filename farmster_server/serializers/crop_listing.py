from rest_framework import serializers, status
from farmster_server.models.crop_listing import CropListing
from farmster_server.serializers.crop import CropSerializer
from farmster_server.serializers.farmer import FarmerFullSerializer
from farmster_server.utils.timestamp_field import TimestampField
from farmster_server.models.crop import Crop
from django.db.models import Count, Sum


class CropListingFullSerializer(serializers.ModelSerializer):
    crop = CropSerializer()
    farmer = FarmerFullSerializer()
    harvest_date = TimestampField()
    #crop_count = serializers.IntegerField()

    #crop_count = serializers.SerializerMethodField()

    # def get_crop_count(self, obj):
    #     return Crop.objects.aggregate(
    #         crop_count=Count('name'),
    #         total_sum=Sum('crop_listings__amount')
    #     )

    class Meta:
        model = CropListing
        fields = ['id', 'crop', 'farmer', 'harvest_date', 'variety', 'amount', 'amount_unit', 'status']
                  #'crop_count']



class CropListingWriteSerializer(serializers.ModelSerializer):
    harvest_date = TimestampField()

    class Meta:
        model = CropListing
        fields = ['crop', 'farmer', 'harvest_date', 'variety', 'amount', 'amount_unit', 'status']


class FarmerByCropListingSerializer(serializers.Serializer):
    crops = serializers.ListField(
        child=serializers.IntegerField(min_value=0, max_value=100000), default=[]
    )
    regions = serializers.ListField(allow_null=True, default=[])
    harvest_time_to = serializers.DateField(allow_null=True, required=False)
    harvest_time_from = serializers.DateField(allow_null=True, required=False)


class CropListingCountSerializer(serializers.ModelSerializer):
    crop_count = serializers.IntegerField()
    #total_sum = serializers.IntegerField(default=0)

    class Meta:
        model = Crop
        fields = ['id', 'name', 'crop_count'] #, 'total_sum']
