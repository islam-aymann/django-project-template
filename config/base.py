from pathlib import Path

import environ
from django.utils.translation import gettext_lazy as _

from config import Environment

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()

ENVIRONMENT = Environment(env("DJANGO_SETTINGS_MODULE"))
if ENVIRONMENT.is_local:
    env.read_env(BASE_DIR / ".env")

# region Django Core Settings

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG", bool, False)
DEBUG_TOOLBAR = env("DEBUG_TOOLBAR", bool, False)

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project_name.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project_name.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE", str, "django.db.backends.postgresql"),
        "NAME": env("POSTGRES_DB", str, str(BASE_DIR / "db.sqlite3")),
        "USER": env("POSTGRES_USER", str, None),
        "PASSWORD": env("POSTGRES_PASSWORD", str, None),
        "HOST": env("POSTGRES_HOST", str, None),
        "PORT": env("POSTGRES_PORT", int, None),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        )
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
ARABIC = "ar"
ENGLISH = "en-us"

LANGUAGE_CODE = ENGLISH

LANGUAGES = [(ARABIC, _("Arabic")), (ENGLISH, _("English"))]

LOCALE_PATHS = []

TIME_ZONE = env("TIME_ZONE", str, "UTC")
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "media/"
MEDIA_DIR = BASE_DIR / "media"
MEDIA_ROOT = MEDIA_DIR

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{levelname}] {asctime} in {pathname}/{funcName}: {message}",
            "style": "{",
        },
        "simple": {
            "format": "[{levelname}] {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "verbose"},
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}
# endregion

# region Third Party Apps
# whitenoise:
# Radically simplified static file serving for Python web apps.
STATICFILES_STORAGE = env(
    "STATICFILES_STORAGE",
    str,
    "whitenoise.storage.CompressedStaticFilesStorage",
)

# djangorestframework:
# Web APIs for Django.
INSTALLED_APPS.append("rest_framework")
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# django-cors-headers:
# A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses.
# This allows in-browser requests to your Django application from other origins.
INSTALLED_APPS.append("corsheaders")
CORS_ALLOW_ALL_ORIGINS = True

# django-storages:
# django-storages is a collection of custom storage backends for Django.
INSTALLED_APPS.append("storages")
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", str, None)
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", str, None)
AWS_S3_FILE_OVERWRITE = env("AWS_S3_FILE_OVERWRITE", bool, False)
AWS_S3_ENDPOINT_URL = env("AWS_S3_ENDPOINT_URL", str, None)
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME", str, None)

# drf-spectacular:
# Sane and flexible OpenAPI 3 schema generation for Django REST framework.
INSTALLED_APPS.append("drf_spectacular")
SPECTACULAR_SETTINGS = {
    "TITLE": "Django Template API",
    "DESCRIPTION": "Django Template API",
    "VERSION": "0.1.0",
    "SERVERS": [{"url": "https://example.com", "description": "Example API Server"}],
    "CONTACT": {"name": "Name", "url": "example.com/api", "email": "admin@example.com"},
    "TAGS": [{"name": "Name", "description": "description"}],
}

# django-solo:
# Helps working with singletons - things like global settings that you want to edit
# from the admin site.
INSTALLED_APPS.append("solo")

# django-jsonform:
# A better, user-friendly JSON editing form field for Django admin.
# Also supports Postgres ArrayField.
INSTALLED_APPS.append("django_jsonform")

# django-ckeditor:
# Django admin CKEditor integration.
INSTALLED_APPS += ["ckeditor"]
CKEDITOR_CONFIGS = {
    "default": {
        "skin": "moono-lisa",
        "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
        "toolbar_Advanced": [
            {
                "name": "document",
                "items": ["Source", "-", "Preview", "Print", "-"],
            },
            {
                "name": "clipboard",
                "items": [
                    "Cut",
                    "Copy",
                    "Paste",
                    "PasteText",
                    "PasteFromWord",
                    "-",
                    "Undo",
                    "Redo",
                ],
            },
            {"name": "editing", "items": ["Find", "Replace", "-", "SelectAll"]},
            {
                "name": "paragraph",
                "items": [
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                    "-",
                    "BidiLtr",
                    "BidiRtl",
                    "Language",
                ],
            },
            {
                "name": "basicstyles",
                "items": ["Bold", "Italic", "Underline", "Strike", "-", "RemoveFormat"],
            },
            {"name": "custom_tools", "items": ["Preview", "Maximize"]},
            {"name": "insert", "items": ["Image", "BulletedList"]},
        ],
        "toolbar": "Advanced",
        "tabSpaces": 4,
    }
}


# endregion

# region Custom Apps

# Core:
# Core app for the project.
INSTALLED_APPS.append("apps.core.apps.CoreConfig")
LOCALE_PATHS.append(BASE_DIR / "apps/core/locale")

# Secondary:
# Secondary app for the project.
INSTALLED_APPS.append("apps.secondary.apps.SecondaryConfig")
LOCALE_PATHS.append(BASE_DIR / "apps/secondary/locale")
# endregion
