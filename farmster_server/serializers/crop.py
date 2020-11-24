from rest_framework import serializers, status
from farmster_server.models.crop import Crop


class CropSerializer(serializers.ModelSerializer):
    #crop_count = serializers.IntegerField()
    #total_sum = serializers.IntegerField(default=0)

    class Meta:
        model = Crop
        fields = ['id', 'name', 'image_url', 'type']#, 'crop_count']  #, 'total_sum']
