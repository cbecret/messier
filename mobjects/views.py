from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mobjects.models import Mobject
from mobjects.serializers import MobjectSerializer

@api_view(['GET', 'POST'])
def mobject_list(request, format=None):
    """
    List all code mobjects, or create a new mobject.
    """
    if request.method == 'GET':
        mobjects = mobject.objects.all()
        serializer = MobjectSerializer(mobjects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MobjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def mobject_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code mobject.
    """
    try:
        mobject = mobject.objects.get(pk=pk)
    except Mobject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MobjectSerializer(mobject)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MobjectSerializer(mobject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mobject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)