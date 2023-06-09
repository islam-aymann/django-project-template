from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampModelMixin(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created"),
    )
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_("modified"),
    )

    class Meta:
        abstract = True
