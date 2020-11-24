from rest_framework import serializers, status
from farmster_server.models.contact import Contact
from farmster_server.services import contact as contact_service


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'location']

    def create(self, validated_data):
        contact = contact_service.create_contact(self.context['request'].user.id, validated_data)
        return contact

