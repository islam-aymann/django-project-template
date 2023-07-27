import socket

from .base import *  # noqa

# django-debug-toolbar:
# A configurable set of panels that display various debug information about the current
# request/response.
INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
DEBUG_TOOLBAR_CONFIG = {"JQUERY_URL": ""}
INTERNAL_IPS = [
    "127.0.0.1",
    socket.gethostbyname(socket.gethostname())[:-1] + "1",
]
