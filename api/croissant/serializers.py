from rest_framework import serializers
from croissant.models import Layer, Start


class StartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Start
        fields = '__all__'


class LayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layer
        fields = '__all__'
