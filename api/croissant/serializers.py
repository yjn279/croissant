from rest_framework import serializers
from croissant.models import Layer


class LayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layer
        fields = ['id', 'title', 'description', 'owner', 'created', 'edited']


# class ProgressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Progress
#         fields = ['id', 'progress', 'layer', 'created']


# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ['id', 'task', 'layer', 'created']


# class ChildSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Child
#         fields = ['id', 'parent', 'child', 'created']


# class ParticipantsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Participants
#         fields = ['id', 'layer', 'user', 'created']


# class StartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Start
#         fields = ['id', 'date', 'time', 'created']


# class EndSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = End
        fields = ['id', 'date', 'time', 'created']
