from rest_framework import serializers
from croissant.models import Layer


class LayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layer
        fields = [
            'id',
            'title',
            'description',
            # 'progress'
            # 'complete'
            'children',
            'participants',
            'owner',
            'start_date'
            'start_time'
            'end_date'
            'end_time'
            'creator',
            'created',
            'edited',
        ]
