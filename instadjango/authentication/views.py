from rest_framework import generics

from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserCreateView(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer
