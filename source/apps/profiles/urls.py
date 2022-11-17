from apps.profiles.views import ProfileUpdateView
from django.urls import path

app_name = "profiles"

urlpatterns = [
    path("profile", view=ProfileUpdateView.as_view(), name="profile"),
]
