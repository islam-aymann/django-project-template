from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.mixins import TimestampModelMixin
from apps.core.models.tag import Tag


class Post(TimestampModelMixin):
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

    author = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name=_("tags"))

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    @property
    def is_published(self) -> bool:
        return self.status == self.Status.PUBLISHED

    def __str__(self):
        return f"Post(id={self.id}, author_id={self.author_id}, title={self.title})"
