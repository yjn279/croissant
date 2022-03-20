from croissant.models import Layer
from croissant.serializers import LayerSerializer
from rest_framework import viewsets


class Layers(viewsets.ModelViewSet):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer


# class Layer(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Layer.objects.all()
#     serializer_class = LayerSerializer
