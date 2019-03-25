from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from .models import MyUser, Profile
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly


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

class ProfileView(APIView):
    #Allow any user to hit this endpoint
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    # renderer_classes = (ProfileJSONRenderer,)

    def get(self, request, user_id, format=None):
        try:
            profile =  Profile.objects.get(user__id=user_id)
            serializer = ProfileSerializer(profile, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response(
                {
                    'message': 'Profile not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, user_id, format=None):
        try:
            serializer_data = request.data.get('user', {})
            serializer = ProfileSerializer(
                request.user.profile,
                data=serializer_data,
                partial=True,
                context={'request': request}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response(
                    {
                        'message': 'Profile not found'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )



