from rest_framework import serializers, status
from rest_framework.exceptions import APIException

from farmster_server.services import place as place_service
from farmster_server.models.place import Place
from farmster_server.serializers.agent import AgentSerializer


class PlaceFullSerializer(serializers.ModelSerializer):
    agents = AgentSerializer(many=True)

    class Meta:
        model = Place
        fields = ['id', 'agents', 'name', 'type', 'district', 'location_lat', 'location_lon', 'country']


class PlaceWithDistanceSerializer(serializers.ModelSerializer):
    agents = AgentSerializer(many=True)
    distance_km = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ['id', 'agents', 'name', 'type', 'district', 'location_lat', 'location_lon', 'country', 'distance_km']

    def get_distance_km(self, place):
        if 'user_lat' in self.context['request'].query_params and 'user_lon' in self.context['request'].query_params:
            user_lat = self.context['request'].query_params['user_lat']
            user_lon = self.context['request'].query_params['user_lon']
        elif 'user_lat' in self.context['request'].data and 'user_lon' in self.context['request'].data:
            user_lat = self.context['request'].data['user_lat']
            user_lon = self.context['request'].data['user_lon']
        else:
            raise APIException("'user_lat' and 'user_lon' are mandatory for PlaceWithDistanceSerializer")

        return place_service.get_user_distance(place, user_lat, user_lon)


class PlaceWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = ['name', 'type', 'district', 'location_lat', 'location_lon', 'country']

