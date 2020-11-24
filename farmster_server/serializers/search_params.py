from rest_framework import serializers
from farmster_server.utils.timestamp_field import TimestampField


class SearchParamsSerializer(serializers.Serializer):
    user_lat = serializers.FloatField()
    user_lon = serializers.FloatField()
    favorite_crops_only = serializers.BooleanField(allow_null=True)
    favorite_places_only = serializers.BooleanField(allow_null=True)
    favorite_farmer_only = serializers.BooleanField(allow_null=True)
    min_distance_km = serializers.FloatField(allow_null=True, default=None)
    max_distance_km = serializers.FloatField(allow_null=True, default=None)
    harvest_time_from = TimestampField(allow_null=True, default=None)
    harvest_time_to = TimestampField(allow_null=True, default=None)
    crops = serializers.ListField(
        child=serializers.IntegerField(min_value=0, max_value=100), default=[]
    )
