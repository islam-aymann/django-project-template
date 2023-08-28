from rest_framework import serializers

from apps.core.api.v1.serializers.author import AuthorSerializer
from apps.core.api.v1.serializers.tag import TagSerializer
from apps.core.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "status",
            "author",
            "tags",
        ]
