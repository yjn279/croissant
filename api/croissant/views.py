from croissant.models import Layer
from croissant.serializers import LayerSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LayersView(APIView):
    def get(self, request, format=None):
        layers = Layer.objects.all()
        serializer = LayerSerializer(layers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LayerView(APIView):
    def get_object(self, pk):
        try:
            return Layer.objects.get(pk=pk)
        except Layer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        layer = self.get_object(pk)
        serializer = LayerSerializer(layer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        layer = self.get_object(pk)
        serializer = LayerSerializer(layer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        layer = self.get_object(pk)
        layer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
