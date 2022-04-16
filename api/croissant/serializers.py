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

        start = validated.pop('starts')[0]
        end = validated.pop('ends')[0]
        layer = super().create(validated)
        
        if (start['date'] or start['time']) is not None:
            layer.starts.create(layer=layer.id, **start)
        
        if (end['date'] or end['time']) is not None:
            layer.ends.create(layer=layer.id, **end)

        return layer


    def update(self, instance, validated):

        start = validated.pop('starts')[0]
        end = validated.pop('ends')[0]
        layer = super().update(instance, validated)

        latest = instance.starts.latest('created')
        if start['date'] != latest.date or start['time'] != latest.time:
            layer.starts.create(layer=layer.id, **start)
        
        latest = instance.ends.latest('created')
        if end['date'] != latest.date or end['time'] != latest.time:
            layer.ends.create(layer=layer.id, **end)

        return layer
