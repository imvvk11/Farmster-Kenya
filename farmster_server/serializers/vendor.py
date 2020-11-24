from rest_framework import serializers
from farmster_server.models.vendor import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"
        read_only_fields = ['vendor_id', 'count']