from croissant.models import Layer, Start
from croissant.serializers import LayerSerializer, StartSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LayersView(APIView):

    def get(self, request, format=None):
        datas = []
        for layer in Layer.objects.all():
            layer = LayerSerializer(layer)
            data = layer.data
            data['start_date'] = data['start'][0]['date']
            data['starta_time'] = data['start'][0]['time']
            _ = data.pop('start')
            datas.append(layer.data)
        return Response(data)

    def post(self, request, format=None):
        start_time = request.data.pop('start_time')
        start_date = request.data.pop('start_date')
        data = request.data
        data['start'] = []
        data['start'].append({'date': start_date, 'time': start_time})
        layer_serializer = LayerSerializer(data=data)
        if layer_serializer.is_valid():
            layer_serializer.save()
            return Response(layer_serializer.data, status=status.HTTP_201_CREATED)
        return Response(layer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LayerView(APIView):

    def get_object(self, pk):
        try:
            return Layer.objects.get(pk=pk)
        except Layer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        layer = self.get_object(pk)
        start = Start.objects.latest('created')
        layer_serializer = LayerSerializer(layer)
        start_serializer = StartSerializer(start)
        print(start_serializer)
        print(start_serializer.data)
        print(type(start_serializer))
        return Response(start_serializer.data)

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
