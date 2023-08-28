from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.secondary.api.v1 import views

router = SimpleRouter()

urlpatterns = router.urls + [
    path("secondary/", views.SecondaryAPIView.as_view(), name="secondary"),
]
