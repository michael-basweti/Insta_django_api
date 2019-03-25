from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post

class PostCreateListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        post = request.data.get('post', {})
        serializer = self.serializer_class(
            data=post,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
