from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from apps.utils import TimeStampedModelMixin


class Profile(TimeStampedModelMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.TextField()
    image = models.ImageField(upload_to="profile", blank=True, null=True)

    last_modified_posts = GenericRelation("Post")

    class Meta:
        abstract = True

    @property
    def full_name(self) -> str:
        return self.user.get_full_name()

    def __str__(self) -> str:
        return self.nickname or self.user.get_full_name()


class Editor(Profile):
    pass


class Author(Profile):
    pass
