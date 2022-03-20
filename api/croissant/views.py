from croissant.models import Layer
from croissant.serializers import LayerSerializer
from rest_framework import viewsets


class LayerViewSet(viewsets.ModelViewSet):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer
