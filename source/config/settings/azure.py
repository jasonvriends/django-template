from config.settings.base import *
from config.settings.base import env
from config.settings.base import DJANGO_APPS, LOCAL_APPS, THIRD_PARTY_APPS, env

# GENERAL
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-trusted-origins
CSRF_TRUSTED_ORIGINS = env.list("DJANGO_CSRF_TRUSTED_ORIGINS", default="[]")

# APPS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps

DJANGO_APPS += [
]

THIRD_PARTY_APPS += [
    "storages",
]

LOCAL_APPS += [
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# STORAGE
# ------------------------------------------------------------------------------
# https://django-storages.readthedocs.io/en/latest/backends/azure.html#settings

DEFAULT_FILE_STORAGE = "config.storage.azure.AzureMediaStorage"
STATICFILES_STORAGE = "config.storage.azure.AzureStaticStorage"

AZURE_ACCOUNT_NAME = env("DJANGO_AZURE_ACCOUNT_NAME", default="")
AZURE_ACCOUNT_KEY = env("DJANGO_AZURE_ACCOUNT_KEY", default="")
AZURE_MEDIA_CONTAINER = env("DJANGO_AZURE_MEDIA_CONTAINER", default="")
AZURE_STATIC_CONTAINER = env("DJANGO_AZURE_STATIC_CONTAINER", default="")

# STATIC
# ------------------------------------------------------------------------------

# AZURE_CUSTOM_DOMAIN = f'{env("DJANGO_AZURE_ACCOUNT_NAME", default="")}.azureedge.net' # CDN URL
AZURE_CUSTOM_DOMAIN = (
    f'{env("DJANGO_AZURE_ACCOUNT_NAME", default="")}.blob.core.windows.net'  # Files URL
)

STATIC_URL = (
    f'https://{AZURE_CUSTOM_DOMAIN}/{env("DJANGO_AZURE_STATIC_CONTAINER", default="")}/'
)
MEDIA_URL = (
    f'https://{AZURE_CUSTOM_DOMAIN}/{env("DJANGO_AZURE_MEDIA_CONTAINER", default="")}/'
)

# django-allauth
# ------------------------------------------------------------------------------

# Email confirmation
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[django-starter]"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# After 10 failed login attempts, restrict logins for 30 minutes
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 1800

# Other settings
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email

# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

# https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = env("DJANGO_EMAIL_USE_TLS", default="True")

# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = env("DJANGO_EMAIL_HOST", default="smtp.sendgrid.net")

# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = env("DJANGO_EMAIL_PORT", default="587")

# https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = env("DJANGO_EMAIL_HOST_USER", default="apikey")

# https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_HOST_PASSWORD", default="")
