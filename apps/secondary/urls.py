from django.urls import path, include

app_name = "secondary"

urlpatterns = [
    path("v1/", include("apps.secondary.api.v1.urls")),
]
