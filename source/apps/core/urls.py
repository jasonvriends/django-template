from apps.core.views import home_view, privacypolicy_view
from django.urls import path

app_name = "core"

urlpatterns = [
    path("", view=home_view, name="home"),
    path("privacy", view=privacypolicy_view, name="privacypolicy"),
]
