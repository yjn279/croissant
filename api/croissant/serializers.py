from rest_framework import serializers
from croissant.models import Layer, Start


class StartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Start
        fields = '__all__'

class LayerSerializer(serializers.ModelSerializer):
    start = StartSerializer(many=True)
    
    class Meta:
        model = Layer
        fields = '__all__'

    def create(self, validated_data):
        start = validated_data.pop('start')
        layer = super().create(validated_data)
        layer.start.create(**start[0], layer=layer)
        return layer
