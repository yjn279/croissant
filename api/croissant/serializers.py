from django.db import models
from rest_framework import serializers
from croissant.models import Layer


class LayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Layer
        fields = ['title', 'description', 'edited']
        read_only_fields = ['id', 'owner', 'created']
