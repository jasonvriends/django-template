from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.profiles"

    def ready(self):
        from apps.profiles.signals import post_delete, pre_save
