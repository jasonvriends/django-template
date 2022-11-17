import uuid

from apps.accounts.managers import UserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    name = models.CharField(verbose_name="full name", max_length=191)

    email = models.EmailField(
        verbose_name="email address",
        unique=True,
        db_index=True,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    def get_name(self):
        return self.name

    def __str__(self):
        return f"{self.email} ({self.name})"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]
