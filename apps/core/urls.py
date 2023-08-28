from django.urls import path, include

from apps.core import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("v1/", include("apps.core.api.v1.urls")),
]
