from rest_framework import generics, viewsets
from rest_framework.response import Response
from croissant.serializers import LayersSerializer
from croissant.models import Layer


class LayersViewSet(viewsets.ModelViewSet):
    serializer_class = LayersSerializer
    queryset = Layer.objects.all()


# class LayersView(generics.ListCreateAPIView):
#     queryset = Layer.objects.all()
#     serializer_class = LayersListSerializer

#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = LayersListSerializer(queryset)
#         return Response(serializer.data)

    # def create(self, request):
    #     queryset = self.get_queryset()
    #     serializer = LayersCreateSerializer(queryset)
    #     return Response(serializer.data)
