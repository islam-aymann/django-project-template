from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.core.api.v1 import views

router = SimpleRouter()
router.register("posts", views.PostViewSet, basename="post")

urlpatterns = router.urls + [
    path("version/", views.APIVersionView.as_view(), name="version"),
]
