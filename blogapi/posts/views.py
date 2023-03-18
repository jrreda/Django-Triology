from rest_framework import generics, permissions

from .models import Post
from .permessions import IsAuthorOrReadOnly
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer
