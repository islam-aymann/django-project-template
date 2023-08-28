from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.core.api.v1.serializers.post import PostSerializer
from apps.core.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("author").prefetch_related("tags").all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
