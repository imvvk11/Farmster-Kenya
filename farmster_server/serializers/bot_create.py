from rest_framework import serializers

from farmster_server.utils.timestamp_field import TimestampField


class BotCreatePlaceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, allow_blank=False)
    district = serializers.CharField(max_length=255, allow_blank=False)
    location_lat = serializers.FloatField()
    location_lon = serializers.FloatField()
    country = serializers.CharField(max_length=2, allow_blank=False)


class BotCreateFarmerSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255, allow_blank=False)
    last_name = serializers.CharField(max_length=255, allow_blank=True, allow_null=True, default='')
    phone_number = serializers.CharField(max_length=255, allow_blank=False)


class BotDealPartsSerializer(serializers.Serializer):
    crop = serializers.IntegerField()
    date = TimestampField()
    shipping_method = serializers.CharField(max_length=255, allow_blank=False)
    price = serializers.FloatField()
    pricing_type = serializers.CharField(max_length=255, allow_blank=False)
    amount = serializers.FloatField()
    amount_unit = serializers.CharField(max_length=255, allow_blank=False)
    crop_quality = serializers.CharField(max_length=255, allow_blank=False)
    crop_size = serializers.CharField(max_length=255, allow_blank=False)
    currency = serializers.CharField(max_length=3, allow_null=False)


class BotCreateDealsSerializer(serializers.Serializer):
    deal_parts = BotDealPartsSerializer(many=True)
    farmer_first_name = serializers.CharField(max_length=255, allow_blank=False)
    farmer_last_name = serializers.CharField(max_length=255, allow_blank=True, allow_null=True, default='')
    farmer_phone_number = serializers.CharField(max_length=255, allow_blank=False)
