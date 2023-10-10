from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse


def get_admin_site_model_change_url(obj: models.Model) -> str:
    app_model = str(ContentType.objects.get_for_model(obj)).replace(" | ", "_")

    return reverse(viewname=f"admin:{app_model}_change", args=[obj.id])
