from .base import *
from ..env_utils import get_env

DEBUG = False

SECRET_KEY = get_env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = get_env("DJANGO_ALLOWED_HOSTS").split(",")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "PORT": get_env("POSTGRES_PORT"),
        "HOST": get_env("POSTGRES_HOST"),
        "NAME": get_env("POSTGRES_DB"),
        "USER": get_env("POSTGRES_USER"),
        "PASSWORD": get_env("POSTGRES_PASSWORD"),
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = get_env("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = get_env("EMAIL_PORT")
EMAIL_HOST_USER = get_env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_env("EMAIL_HOST_PASSWORD")
