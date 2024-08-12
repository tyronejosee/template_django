"""Settings for config project (Local)."""

import os
import sys
from .base import *


DEBUG = True

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

INTERNAL_IPS = [
    "127.0.0.1",
    "http://127.0.0.1:8000/",
    "localhost",
]


if "test" in sys.argv:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "dropdash_db",
            "USER": "dropdash_user",
            "PASSWORD": "dropdash_password",
            "HOST": "db",
            "PORT": "5432",
        }
    }


STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
