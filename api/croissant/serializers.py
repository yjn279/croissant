from rest_framework import serializers
from croissant.models import Layer


class LayerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=64, allow_blank=True, default='')
    description = serializers.CharField(allow_blank=True, default='')
    children = serializers.IntegerField()
    tasks = serializers.IntegerField(default=1)
    progress = serializers.IntegerField(default=0)
    owner = serializers.IntegerField()
    participants = serializers.IntegerField()
    start_date = serializers.DateField()
    start_time = serializers.TimeField()
    end_date = serializers.DateField()
    end_time = serializers.TimeField()
    created = serializers.DateTimeField()
    edited = serializers.DateTimeField()

    def create(self, validated_data):
        return Layer(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.children = validated_data.get('children', instance.children)
        instance.tasks = validated_data.get('tasks', instance.tasks)
        instance.progress = validated_data.get('progress', instance.progress)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.participants = validated_data.get('participants', instance.participants)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.created = validated_data.get('created', instance.created)
        instance.edited = validated_data.get('edited', instance.edited)
        instance.save()
        return instance
