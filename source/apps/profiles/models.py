from apps.profiles.utils import image_resize
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Profile(models.Model):

    # Generate available timezones for user profile
    timezones = []
    for mytimezone in timezone.zoneinfo.available_timezones():
        temp = [mytimezone, mytimezone]
        timezones.append(temp)
    timezones.sort()

    id = models.BigAutoField(primary_key=True, editable=False)

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)

    timezone = models.CharField(
        verbose_name=("Timezone"),
        choices=timezones,
        default="UTC",
        max_length=120,
    )

    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)

    THEME_CHOICES = (("light", "Light"), ("dark", "Dark"))

    theme = models.CharField(max_length=10, choices=THEME_CHOICES, default="light")

    def __str__(self):
        return f"{self.user.email} ({self.user.name})"

    def save(self, *args, **kwargs):
        if self.image:
            image_resize(self.image, 150, 150)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
