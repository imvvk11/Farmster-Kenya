from rest_framework import serializers
from farmster_server.models.agent import Agent


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'first_name', 'last_name', 'phone_number']
