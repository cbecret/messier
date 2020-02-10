from mobjects.models import Mobject
from mobjects.serializers import MobjectSerializer
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from mobjects.serializers import UserSerializer
from mobjects.permissions import IsOwnerOrReadOnly


class MobjectViewSet(viewsets.ModelViewSet):
    queryset = Mobject.objects.all()
    serializer_class = MobjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'mobjects': reverse('mobject-list', request=request, format=format)
    })

