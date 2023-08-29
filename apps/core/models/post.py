from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.profiles import Editor, Author
from apps.core.models.tag import Tag
from apps.utils import TimeStampedModelMixin


class Post(TimeStampedModelMixin):
    class Status(models.TextChoices):
        DRAFT = "DR", _("Draft")
        APPROVED = "AP", _("Approved")
        PUBLISHED = "PU", _("Published")
        DELETED = "DE", _("Deleted")

    title = models.CharField(max_length=512, verbose_name=_("title"))
    content = models.TextField(verbose_name=_("content"))
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name=_("status"),
    )

    author = models.ForeignKey(
        Author,
        verbose_name=_("author"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    editor = models.ForeignKey(
        Editor,
        verbose_name=_("editor"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    content_type = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    object_id = models.PositiveIntegerField(blank=True, null=True)
    last_modified_by = GenericForeignKey("content_type", "object_id")

    tags = models.ManyToManyField(Tag, verbose_name=_("tags"))

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

    @property
    def is_published(self) -> bool:
        return self.status == self.Status.PUBLISHED

    def __str__(self):
        return f"Post(id={self.id}, author_id={self.author_id}, title={self.title})"
