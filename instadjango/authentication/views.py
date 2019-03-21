from rest_framework import generics, status
from rest_framework.views import APIView
from .models import MyUser
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response


class UserCreateView(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

class LoginApiView(APIView):
    permission_classes = ()

    def post(self, request, format=None):
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        user = authenticate(email=email, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

