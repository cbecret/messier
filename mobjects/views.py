from mobjects.models import Mobject
from mobjects.serializers import MobjectSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from mobjects.serializers import UserSerializer
from mobjects.permissions import IsOwnerOrReadOnly


class MobjectList(generics.ListCreateAPIView):
    queryset = Mobject.objects.all()
    serializer_class = MobjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MobjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mobject.objects.all()
    serializer_class = MobjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer