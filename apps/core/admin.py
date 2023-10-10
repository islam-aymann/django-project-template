from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from solo.admin import SingletonModelAdmin

from apps.core.models import Tag, Post, SiteConfiguration, AuditTrail, Author
from apps.utils import get_admin_site_model_change_url

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


@admin.register(AuditTrail)
class AuditTrailAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "action",
        "user",
        "target",
        "from_object",
        "to_object",
    ]

    list_select_related = [
        "user",
        "target_content_type",
        "from_content_type",
        "to_content_type",
    ]

    def target(self, obj) -> str:
        url = reverse(
            f"admin:{obj.target_object._meta.app_label}_{obj.target_object._meta.model_name}_change",
            args=[obj.target_object_id],
        )

        return format_html(f'<a href="{url}">{obj.target_object}</a>')

    def from_object(self, obj) -> str:
        if not obj.from_object:
            return ""

        url = get_admin_site_model_change_url(obj.from_object)

        return format_html(f'<a href="{url}">{obj.from_object}</a>')

    def to_object(self, obj) -> str:
        if not obj.to_object:
            return ""

        url = get_admin_site_model_change_url(obj.to_object)

        return format_html(f'<a href="{url}">{obj.to_object}</a>')

    def action(self, obj) -> str:
        return obj.get_action_display()

    to_object.short_description = _("To")
    from_object.short_description = _("From")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "nickname", "phone", "address", "image"]
    search_fields = ["nickname", "phone", "address"]
    list_filter = ["nickname", "phone", "address"]
    raw_id_fields = ["user"]
