from rest_framework import serializers
from croissant.models import Layer, Start


class StartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Start
        fields = '__all__'


class LayersSerializer(serializers.ModelSerializer):
    start = StartSerializer()
    
    class Meta:
        model = Layer
        fields = '__all__'

    def create(self, validated_data):
        start_data = validated_data.pop('start')
        layer = super().create(validated_data)
        start_data['layer'] = layer
        start = Start.objects.create(**start_data)
        layer.start.add(start)
        return layer
