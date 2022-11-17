from config.settings.base import *
from config.settings.base import env

# GENERAL
# ------------------------------------------------------------------------------

# APPS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps

DJANGO_APPS += [
]

THIRD_PARTY_APPS += [
]

LOCAL_APPS += [
]

# EMAIL
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)
