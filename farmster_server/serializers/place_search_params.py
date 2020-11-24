from rest_framework import serializers


class PlaceSearchParamsSerializer(serializers.Serializer):
    user_lat = serializers.FloatField()
    user_lon = serializers.FloatField()
    text = serializers.CharField(allow_blank=True, max_length=100, required=False)


class FavoriteOnlyParamsSerializer(serializers.Serializer):
    favorite_crops_only = serializers.BooleanField()
