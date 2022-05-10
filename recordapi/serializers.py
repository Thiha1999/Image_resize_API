from rest_framework import serializers

from recordapi.models import Fish

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = ('id', 'fishname', 'species', 'weight', 'length', 'latitude', 'longitude', 'image', 'uploaded')

