from croissant.models import Layer
from croissant.serializers import LayerSerializer
from rest_framework import generics


class Layers(generics.ListCreateAPIView):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer


class Layer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer
