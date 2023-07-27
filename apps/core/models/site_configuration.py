from typing import Dict, Any

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jsonform.models.fields import JSONField
from solo.models import SingletonModel
from apps.core.models.tag import Tag


def generate_tag_colors_schema() -> Dict[str, Any]:
    tags = Tag.objects.all()

    schema = {
        "type": "object",
        "keys": {
            f"{tag.pk}": {
                "title": str(tag),
                "type": "object",
                "properties": {
                    "value": {"type": "string", "format": "color"},
                },
                "required": ["value"],
            }
            for tag in tags
        },
    }

    return schema


class SiteConfiguration(SingletonModel):
    name = models.CharField(max_length=255, default="Site Name")
    description = models.TextField(default="Site Description")
    maintenance_mode = models.BooleanField(default=False)
    tag_colors = JSONField(default=dict, schema=generate_tag_colors_schema)

    class Meta:
        verbose_name = _("Site Configuration")
        verbose_name_plural = _("Site Configuration")

    def __str__(self) -> str:
        return str(_("Site Configuration"))
