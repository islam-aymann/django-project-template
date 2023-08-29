# Generated by Django 4.2.4 on 2023-08-29 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("core", "0003_author_editor_remove_post_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content_type",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to=models.Q(
                    ("app_label", "core"), ("model__in", ["editor", "author"])
                ),
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="contenttypes.contenttype",
            ),
        ),
    ]
