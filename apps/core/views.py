from django.contrib.auth.models import User
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render

from apps.core.models import Post, Tag


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def home(request: HttpRequest) -> JsonResponse:
    first_post = Post.objects.select_related("author").prefetch_related("tags").first()

    if not first_post:
        user = User.objects.filter(username="username").first()

        if not user:
            user = User.objects.create_user(
                username="username",
                first_name="John",
                last_name="Doe",
                email="admin@exmaple.com",
                password="veryBadPassword",
            )

        first_post = Post.objects.create(
            title="Hello World",
            content="Hello World",
            status=Post.Status.PUBLISHED,
            author=user,
        )

        tags = [Tag.objects.create(name=f"tag{i}") for i in range(10)]

        first_post.tags.add(*tags)

    return JsonResponse(
        {
            "id": first_post.id,
            "title": first_post.title,
            "content": first_post.content,
            "status": first_post.status,
            "is_published": first_post.is_published,
            "author_id": first_post.author_id,
            "created": first_post.created,
            "modified": first_post.modified,
            "author": {
                "id": first_post.author.id,
                "username": first_post.author.username,
                "first_name": first_post.author.first_name,
                "last_name": first_post.author.last_name,
                "email": first_post.author.email,
                "is_staff": first_post.author.is_staff,
                "is_active": first_post.author.is_active,
                "date_joined": first_post.author.date_joined,
            },
            "tags": [{"id": tag.id, "name": tag.name} for tag in first_post.tags.all()],
        },
        json_dumps_params={"indent": 4},
    )
