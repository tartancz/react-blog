from .base import *

SECRET_KEY = "+8jce$epoxo4)cs(8h+mu=th^as=r*h@o)=sll1^grlx)j%jh3"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "dev",
        "USER": "dev",
        "PASSWORD": "dev",
        "HOST": "localhost",
        "PORT": 5432,
    }
}
