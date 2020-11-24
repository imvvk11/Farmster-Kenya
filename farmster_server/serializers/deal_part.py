from rest_framework import serializers, status
from farmster_server.models.deal_part import DealPart
from farmster_server.serializers.crop import CropSerializer
from farmster_server.utils.timestamp_field import TimestampField


class DealPartsFullSerializer(serializers.ModelSerializer):
    crop = CropSerializer()
    date = TimestampField()

    class Meta:
        model = DealPart
        fields = ['crop', 'date', 'shipping_method', 'currency', 'price', 'pricing_type', 'amount',
                  'amount_unit', 'crop_quality', 'crop_size']


class DealPartsWriteSerializer(serializers.ModelSerializer):
    date = TimestampField()

    class Meta:
        model = DealPart
        fields = ['crop', 'date', 'shipping_method', 'currency', 'price', 'pricing_type', 'amount',
                  'amount_unit', 'crop_quality', 'crop_size']

