from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from solo.admin import SingletonModelAdmin

from apps.core.models import Tag, Post, SiteConfiguration

admin.site.site_header = _("Project Name")
admin.site.site_title = _("Project Name")


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(SingletonModelAdmin):
    list_display = ["id", "name", "description", "maintenance_mode", "tag_colors"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_select_related = ["author", "author__user"]
    raw_id_fields = ["author"]
    list_display = ["id", "title", "status", "author", "last_modified_by", "created_at"]
    list_filter = ["title", "status", "author", "created_at"]
    search_fields = ["title", "content", "tags__name"]
    filter_horizontal = ["tags"]
