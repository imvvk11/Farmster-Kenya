from rest_framework import serializers
from farmster_server.models.farmer import Farmer
from farmster_server.serializers.place import PlaceFullSerializer


class FarmerFullSerializer(serializers.ModelSerializer):
    places = PlaceFullSerializer(many=True)

    class Meta:
        model = Farmer
        fields = ['id', 'places', 'first_name', 'last_name', 'phone_number']


class FarmerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['phone_number', 'first_name', 'last_name']
