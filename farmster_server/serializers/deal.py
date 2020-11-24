from rest_framework import serializers, status
from farmster_server.models.deal import Deal
from farmster_server.services import deal as deal_service
from farmster_server.services import deal_part as deal_part_service
from farmster_server.serializers import deal_part as deal_parts_serializer
from farmster_server.serializers import farmer as farmer_serializer


class DealFullSerializer(serializers.ModelSerializer):
    deal_parts = deal_parts_serializer.DealPartsFullSerializer(many=True)
    farmer = farmer_serializer.FarmerFullSerializer()

    class Meta:
        model = Deal
        fields = ['deal_parts', 'id', 'farmer']


class DealWriteSerializer(serializers.ModelSerializer):
    deal_parts = deal_parts_serializer.DealPartsWriteSerializer(many=True)

    class Meta:
        model = Deal
        fields = ['deal_parts', 'id', 'farmer']

    def create(self, validated_data):

        deal_parts_data = validated_data.pop('deal_parts')
        deal = deal_service.create_deal(self.context['request'].user.id, validated_data)
        for deal_part in deal_parts_data:
            deal_part_service.create_deal_part(deal, deal_part)
        return deal

    def update(self, instance, validated_data):
        deal_parts_data = validated_data.pop('deal_parts')
        deal_parts = instance.deal_parts.get()

        deal_service.update_deal(instance, validated_data)
        deal_part_service.update_deal_part(deal_parts, deal_parts_data)

        return instance
