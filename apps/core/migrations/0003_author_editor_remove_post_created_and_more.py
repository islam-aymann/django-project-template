# Generated by Django 4.2.4 on 2023-08-28 23:17

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contenttypes", "0002_remove_content_type_name"),
        ("core", "0002_siteconfiguration"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("nickname", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=255)),
                ("address", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="profile"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Editor",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("nickname", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=255)),
                ("address", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="profile"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="post",
            name="created",
        ),
        migrations.RemoveField(
            model_name="post",
            name="modified",
        ),
        migrations.AddField(
            model_name="post",
            name="content_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="object_id",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddIndex(
            model_name="post",
            index=models.Index(
                fields=["content_type", "object_id"],
                name="core_post_content_001f5c_idx",
            ),
        ),
        migrations.AddField(
            model_name="editor",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="author",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="editor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.editor",
                verbose_name="editor",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.author",
                verbose_name="author",
            ),
        ),
    ]
