from django.contrib.auth.models import User
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render

from apps.core.models import Post, Tag, Author


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def home(request: HttpRequest) -> JsonResponse:
    first_post = (
        Post.objects.select_related("author", "author__user")
        .prefetch_related("tags")
        .first()
    )

    if not first_post:
        user = User.objects.first()
        author, _ = Author.objects.get_or_create(
            user=user,
            defaults={
                "nickname": "John",
                "phone": "+201234567890",
                "address": "Cairo, Egypt",
            },
        )

        first_post = Post.objects.create(
            title="Hello World",
            content="Hello World",
            status=Post.Status.PUBLISHED,
            author=author,
        )

        tags = [Tag.objects.create(name=f"tag{i}") for i in range(10)]

        first_post.tags.add(*tags)

    return JsonResponse(
        {
            "id": first_post.id,
            "title": first_post.title,
            "content": first_post.content,
            "status": first_post.get_status_display(),
            "is_published": first_post.is_published,
            "author_id": first_post.author_id,
            "created_at": first_post.created_at,
            "updated_at": first_post.updated_at,
            "author": {
                "id": first_post.author.id,
                "author_user_id": first_post.author.id,
                "first_name": first_post.author.user.first_name,
                "nickname": first_post.author.user.username,
                "phone": first_post.author.phone,
                "email": first_post.author.user.email,
                "is_staff": first_post.author.user.is_staff,
                "is_active": first_post.author.user.is_active,
                "date_joined": first_post.author.user.date_joined,
            },
            "tags": [{"id": tag.id, "name": tag.name} for tag in first_post.tags.all()],
        },
        json_dumps_params={"indent": 4},
    )
