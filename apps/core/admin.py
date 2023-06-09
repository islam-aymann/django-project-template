from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.models import Tag, Post

admin.site.site_header = _("Project Name")
admin.site.site_title = _("Project Name")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]

    search_fields = [
        "name",
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_select_related = [
        "author",
    ]

    raw_id_fields = [
        "author",
    ]

    list_display = [
        "id",
        "title",
        "status",
        "author",
        "created",
    ]

    list_filter = [
        "title",
        "status",
        "author",
        "created",
    ]

    search_fields = [
        "title",
        "content",
        "tags__name",
    ]

    filter_horizontal = [
        "tags",
    ]
