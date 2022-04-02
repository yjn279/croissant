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

    def create(self, validated):
        start = validated.pop('start')
        layer = super().create(validated)
        layer.start.create(layer=layer.id, **start[0])
        return layer

    def update(self, instance, validated):
        start = validated.pop('start')
        layer = super().update(instance, validated)
        layer.start.create(layer=layer.id, **start[0])
        return layer
