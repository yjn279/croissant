from croissant.models import Layer, Start
from croissant.serializers import LayerSerializer, StartSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LayersView(APIView):


    def get(self, request, format=None):

        data = []
        for layer in Layer.objects.all():

            start = StartSerializer(layer.start.latest('created')).data
            layer = LayerSerializer(layer).data

            start['start_date'] = start['date']
            start['start_time'] = start['time']

            del start['id'], start['layer'], start['date'], start['time']
            data.append({**layer, **start})

        return Response(data)


    def post(self, request, format=None):

        start = {
            'date': request.data.pop('start_date'),
            'time': request.data.pop('start_time')
        }

        # Layer
        layer = LayerSerializer(data=request.data)

        if layer.is_valid():
            layer.save()
        else:
            return Response(layer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Start
        start['layer'] = layer.data['id']
        start = StartSerializer(data=start)

        if start.is_valid():
            start.save()
        else:
            return Response(start.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(layer.data, status=status.HTTP_201_CREATED)



class LayerView(APIView):


    def get_object(self, pk):
        try:
            return Layer.objects.get(pk=pk)
        except Layer.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        
        layer = self.get_object(pk)

        # Start
        start = StartSerializer(layer.start.latest('created')).data
        start['start_date'] = start['date']
        start['start_time'] = start['time']
        del start['id'], start['layer'], start['date'], start['time']

        # Layer
        layer = LayerSerializer(layer).data
        del layer['start']

        data = {**layer, **start}
        return Response(data)


    def put(self, request, pk, format=None):

        layer = self.get_object(pk)

        # # Start
        # start_date = request.data.pop('start_date')
        # start_time = request.data.pop('start_time')
        # request.data['start'] = [{'date': start_date, 'time': start_time}]

        # # Layer
        # layer_serializer = LayerSerializer(data=request.data)

        # # Start
        # start_date = request.data.pop('start_date')
        # start_time = request.data.pop('start_time')
        # start = [{'date': start_date, 'time': start_time}]
        # start = StartSerializer(layer.start.latest('created')).data
        # start['start_date'] = start['date']
        # start['start_time'] = start['time']
        # del start['id'], start['layer'], start['date'], start['time']

        # # Layer
        # layer = LayerSerializer(layer).data
        # del layer['start']

        # serializer = LayerSerializer(layer, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        layer = self.get_object(pk)
        layer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
