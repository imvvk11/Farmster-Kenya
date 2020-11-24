from rest_framework import serializers, status

from farmster_server.models.place import Place
from farmster_server.serializers.agent import AgentSerializer


class PlaceForSearchSerializer(serializers.ModelSerializer):
    agents = AgentSerializer(many=True)
    crops_listings_count = serializers.IntegerField()
    distance_km = serializers.FloatField()

    class Meta:
        model = Place
        fields = ['id', 'crops_listings_count', 'distance_km', 'agents', 'name', 'district',
                  'type', 'location_lat', 'location_lon', 'country']
