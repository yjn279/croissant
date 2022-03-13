from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from croissant.models import Layer
from croissant.serializers import LayerSerializer


@csrf_exempt
def layers_list(request):
    """
    List all code layers, or create a new layer.
    """
    if request.method == 'GET':
        layers = Layer.objects.all()
        serializer = LayerSerializer(layers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def layer_detail(request, pk):
    """
    Retrieve, update or delete a code layer.
    """
    try:
        layer = Layer.objects.get(pk=pk)
    except Layer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LayerSerializer(layer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LayerSerializer(layer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        layer.delete()
        return HttpResponse(status=204)
