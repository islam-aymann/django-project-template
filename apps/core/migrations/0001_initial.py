# Generated by Django 4.2.2 on 2023-06-09 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=512, verbose_name="name")),
            ],
            options={
                "verbose_name": "tag",
                "verbose_name_plural": "tags",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "modified",
                    models.DateTimeField(auto_now=True, verbose_name="modified"),
                ),
                ("title", models.CharField(max_length=512, verbose_name="title")),
                ("content", models.TextField(verbose_name="content")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("DR", "Draft"),
                            ("AP", "Approved"),
                            ("PU", "Published"),
                            ("DE", "Deleted"),
                        ],
                        default="DR",
                        max_length=2,
                        verbose_name="status",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="author",
                    ),
                ),
                ("tags", models.ManyToManyField(to="core.tag", verbose_name="tags")),
            ],
            options={
                "verbose_name": "post",
                "verbose_name_plural": "posts",
            },
        ),
    ]
