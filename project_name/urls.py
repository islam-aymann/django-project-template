from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls", namespace="core")),
    path("", include("apps.secondary.urls", namespace="secondary")),
]

if settings.DEBUG and settings.DEBUG_TOOLBAR:
    try:
        import debug_toolbar

        urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    except ImportError:
        pass
