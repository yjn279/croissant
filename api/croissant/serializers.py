from rest_framework import serializers
from croissant.models import Layer, Start


class StartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Start
        fields = '__all__'


class LayerSerializer(serializers.ModelSerializer):
    start = StartSerializer(many=True, allow_null=True)

    class Meta:
        model = Layer
        fields = '__all__'

    def create(self, validated_data):
        start_data = validated_data.pop('start')
        layer = super().create(validated_data)
        layer.start.create(layer=layer.id, **start_data[0])
        return layer
