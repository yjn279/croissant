from rest_framework import serializers
from croissant.models import Layer


class LayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layer
        fields = ['id', 'title', 'text']
