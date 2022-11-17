from apps.profiles.models import Profile
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
