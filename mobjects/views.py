from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.response import Response

from mobjects.models import Mobject
from mobjects.permissions import IsOwnerOrReadOnly
from mobjects.serializers import MobjectSerializer, UserSerializer


# Serializer pour les objets de Messier
class MobjectViewSet(viewsets.ModelViewSet):
    queryset = Mobject.objects.all()
    serializer_class = MobjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Serializer pour les utilisateurs
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
