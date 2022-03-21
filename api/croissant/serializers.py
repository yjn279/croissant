from asyncio import tasks
from asyncore import read
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from croissant.models import Layer


class LayerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    tasks = serializers.IntegerField(min_value=1, read_only=True)
    progress = serializers.IntegerField(min_value=0, read_only=True)
    owner = serializers.CharField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    edited = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Layer
        fields = [
            'id',
            'title',
            'description',
            'children',
            'tasks',
            'progress',
            'owner',
            'participants', 
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'created',
            'edited',
        ]
