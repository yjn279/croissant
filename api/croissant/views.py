from rest_framework import viewsets
from croissant.models import Layer
from croissant.serializers import LayerSerializer


class LayerViewSet(viewsets.ModelViewSet):
    serializer_class = LayerSerializer
    queryset = Layer.objects.all()
