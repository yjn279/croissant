from croissant.models import Layer
from croissant.serializers import LayerSerializer, StartSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LayersView(APIView):


    def get(self, request, format=None):

        data = []
        for layer in Layer.objects.all():

            layer = LayerSerializer(layer).data

            start = layer.pop('start')[-1]
            layer['start_date'] = start['date']
            layer['start_time'] = start['time']
            data.append({**layer})

        return Response(data)


    def post(self, request, format=None):

        request.data['start'] = [{
            'date': request.data.pop('start_date'),
            'time': request.data.pop('start_time')
        }]

        layer = LayerSerializer(data=request.data)

        if layer.is_valid():

            layer.save()

            data = layer.data
            start = data.pop('start')
            data['start_date'] = start[-1]['date']
            data['start_time'] = start[-1]['time']

            return Response(data, status=status.HTTP_201_CREATED)

        else:
            return Response(layer.errors, status=status.HTTP_400_BAD_REQUEST)


class LayerView(APIView):


    def get_object(self, pk):
        try:
            return Layer.objects.get(pk=pk)
        except Layer.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        
        layer = self.get_object(pk)
        layer = LayerSerializer(layer).data

        start = layer.pop('start')[-1]
        layer['start_date'] = start['date']
        layer['start_time'] = start['time']

        return Response({**layer})


    def put(self, request, pk, format=None):

        layer = self.get_object(pk)

        request.data['start'] = [{
            'date': request.data.pop('start_date'),
            'time': request.data.pop('start_time')
        }]

        layer = LayerSerializer(layer, data=request.data)

        if layer.is_valid():

            layer.save()
            
            data = layer.data
            start = data.pop('start')
            data['start_date'] = start[-1]['date']
            data['start_time'] = start[-1]['time']
        
            return Response(data, status=status.HTTP_201_CREATED)

        else:
            return Response(layer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        layer = self.get_object(pk)
        layer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChildrenView(APIView):

    
    def get(self, request, pk, format=None):

        data = []
        for layer in Layer.objects.all().filter(parent__id=pk):

            layer = LayerSerializer(layer).data

            start = layer.pop('start')[-1]
            layer['start_date'] = start['date']
            layer['start_time'] = start['time']
            data.append({**layer})

        return Response(data)


    def post(self, request, pk, format=None):

        request.data['parent'] = pk
        request.data['start'] = [{
            'date': request.data.pop('start_date'),
            'time': request.data.pop('start_time')
        }]

        layer = LayerSerializer(data=request.data)

        if layer.is_valid():

            layer.save()

            data = layer.data
            start = data.pop('start')
            data['start_date'] = start[-1]['date']
            data['start_time'] = start[-1]['time']

            return Response(data, status=status.HTTP_201_CREATED)

        else:
            return Response(layer.errors, status=status.HTTP_400_BAD_REQUEST)
