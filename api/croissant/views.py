from turtle import title
from croissant.models import Layer
from croissant.serializers import LayerSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def pop(dict, key):
    if key in dict:
        return dict.pop(key)
    else:
        None


def format_serialized(layer):

    data = layer.data

    starts = data.pop('starts')
    if starts:
        start = starts[-1]
        data['start_date'] = start['date']
        data['start_time'] = start['time']
    else:
        data['start_date'] = None
        data['start_time'] = None

    ends = data.pop('ends')
    if ends:
        end = ends[-1]
        data['end_date'] = end['date']
        data['end_time'] = end['time']
    else:
        data['end_date'] = None
        data['end_time'] = None

    return data


def format_request(request):

    title = pop(request.data, 'title')
    request.data['title'] = title if title is not None else ''

    description = pop(request.data, 'description')
    request.data['description'] = description if description is not None else ''

    request.data['starts'] = [{
        'date': pop(request.data, 'start_date'),
        'time': pop(request.data, 'start_time')
    }]

    request.data['ends'] = [{
        'date': pop(request.data, 'end_date'),
        'time': pop(request.data, 'end_time')
    }]

    return request


class LayersView(APIView):


    def get(self, request, format=None):

        data = []
        for layer in Layer.objects.all():
            layer = LayerSerializer(layer)
            layer = format_serialized(layer)
            data.append({**layer})

        return Response(data)


    def post(self, request, format=None):

        request = format_request(request)
        layer = LayerSerializer(data=request.data)

        if layer.is_valid():
            layer.save()
            layer = format_serialized(layer)
            return Response(layer, status=status.HTTP_201_CREATED)

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
        layer = LayerSerializer(layer)
        layer = format_serialized(layer)
        return Response({**layer})


    def put(self, request, pk, format=None):

        request = format_request(request)
        layer = self.get_object(pk)
        layer = LayerSerializer(layer, data=request.data)

        if layer.is_valid():
            layer.save()
            layer = format_serialized(layer)
            return Response(layer, status=status.HTTP_201_CREATED)

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
            layer = LayerSerializer(layer)
            layer = format_serialized(layer)
            data.append({**layer})

        return Response(data)


    def post(self, request, pk, format=None):

        request.data['parent'] = pk
        request = format_request(request)
        layer = LayerSerializer(data=request.data)

        if layer.is_valid():
            layer.save()
            layer = format_serialized(layer)
            return Response(layer, status=status.HTTP_201_CREATED)

        else:
            return Response(layer.errors, status=status.HTTP_400_BAD_REQUEST)
