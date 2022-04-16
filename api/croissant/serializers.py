from email.policy import default
from rest_framework import serializers
from croissant.models import Layer, Start, End


class StartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Start
        fields = '__all__'


class EndSerializer(serializers.ModelSerializer):
    class Meta:
        model = End
        fields = '__all__'


class LayerSerializer(serializers.ModelSerializer):
    starts = StartSerializer(allow_null=True, many=True)
    ends = EndSerializer(allow_null=True, many=True)

    class Meta:
        model = Layer
        fields = '__all__'

    def create(self, validated):
        starts = validated.pop('starts')
        ends = validated.pop('ends')
        layer = super().create(validated)
        layer.starts.create(layer=layer.id, **starts[0])
        layer.ends.create(layer=layer.id, **ends[0])
        return layer

    def update(self, instance, validated):
        starts = validated.pop('starts')
        ends = validated.pop('ends')
        layer = super().update(instance, validated)
        layer.starts.create(layer=layer.id, **starts[0])
        layer.ends.create(layer=layer.id, **ends[0])
        return layer
