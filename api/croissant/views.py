from rest_framework import generics, viewsets
from rest_framework.response import Response
from croissant.serializers import LayersSerializer
from croissant.models import Layer


class LayersViewSet(viewsets.ModelViewSet):
    serializer_class = LayersSerializer
    queryset = Layer.objects.all()
