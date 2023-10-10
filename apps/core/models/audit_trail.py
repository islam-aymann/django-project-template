from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils import TimeStampedModelMixin


class AuditTrail(TimeStampedModelMixin):
    class Action(models.TextChoices):
        CREATED = "CR", _("Created")
        UPDATED = "UP", _("Updated")
        REASSIGNED = "RS", _("Reassigned")
        DISABLED = "DS", _("Disabled")
        DELETED = "DL", _("Deleted")

    action = models.CharField(
        verbose_name=_("Action"),
        max_length=255,
        choices=Action.choices,
        default=Action.CREATED,
    )
    description = models.TextField(
        verbose_name=_("Description"),
        default="Audit Trail Description",
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )

    target_content_type = models.ForeignKey(
        to=ContentType,
        on_delete=models.CASCADE,
        related_name="target_content_type",
        verbose_name=_("Target Content Type"),
    )
    target_object_id = models.PositiveIntegerField(verbose_name=_("Target Object ID"))
    target_object = GenericForeignKey(
        ct_field="target_content_type",
        fk_field="target_object_id",
    )

    from_content_type = models.ForeignKey(
        to=ContentType,
        on_delete=models.CASCADE,
        verbose_name=_("From Content Type"),
        blank=True,
        null=True,
        related_name="from_content_type",
    )
    from_object_id = models.PositiveIntegerField(
        verbose_name=_("From Object ID"),
        blank=True,
        null=True,
    )
    from_object = GenericForeignKey(
        ct_field="from_content_type",
        fk_field="from_object_id",
    )

    to_content_type = models.ForeignKey(
        to=ContentType,
        on_delete=models.CASCADE,
        verbose_name=_("To Content Type"),
        blank=True,
        null=True,
        related_name="to_content_type",
    )
    to_object_id = models.PositiveIntegerField(
        verbose_name=_("To Object ID"),
        blank=True,
        null=True,
    )
    to_object = GenericForeignKey(ct_field="to_content_type", fk_field="to_object_id")

    class Meta:
        verbose_name = _("Audit Trail")
        verbose_name_plural = _("Audit Trails")

        indexes = [
            models.Index(fields=["target_content_type", "target_object_id"]),
            models.Index(fields=["from_content_type", "from_object_id"]),
            models.Index(fields=["to_content_type", "to_object_id"]),
        ]

    def __str__(self) -> str:
        return f"AuditTrail(id={self.id}, action={self.action})"
