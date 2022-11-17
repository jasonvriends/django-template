from config.settings.base import env
from django.conf import settings


def templatetags(request):
    tags = {
        "PROJECT_NAME": env("PROJECT_NAME", default="PROJECT_NAME"),
        "PROJECT_PRIVACY_COUNTRY" : env("PROJECT_PRIVACY_COUNTRY", default="PROJECT_PRIVACY_COUNTRY"),
        "PROJECT_PRIVACY_EMAIL" : env("PROJECT_PRIVACY_EMAIL", default="PROJECT_PRIVACY_EMAIL"),
        "PROJECT_PRIVACY_SOCIALACCOUNTS" : env("PROJECT_PRIVACY_SOCIALACCOUNTS", default="PROJECT_PRIVACY_SOCIALACCOUNTS").split(' '),
        "PROJECT_PRIVACY_MODIFIED" : env("PROJECT_PRIVACY_MODIFIED", default="PROJECT_PRIVACY_MODIFIED"),
        "PROJECT_PRIVACY_WEBSITE": env("PROJECT_PRIVACY_WEBSITE", default="PROJECT_PRIVACY_WEBSITE"),
    }
    return(tags)

