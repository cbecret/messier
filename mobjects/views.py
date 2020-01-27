from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from mobjects.models import Mobject
from mobjects.serializers import MobjectSerializer

@csrf_exempt
def mobject_list(request):
    """
    List all code mobjects, or create a new mobject.
    """
    if request.method == 'GET':
        mobjects = Mobject.objects.all()
        serializer = MobjectSerializer(mobjects, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MobjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def mobject_detail(request, pk):
    """
    Retrieve, update or delete a code mobject.
    """
    try:
        mobject = Mobject.objects.get(pk=pk)
    except Mobject.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MobjectSerializer(mobject)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MobjectSerializer(mobject, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        mobject.delete()
        return HttpResponse(status=204)