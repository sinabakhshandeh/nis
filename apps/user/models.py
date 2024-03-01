import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .maganers import CustomUserManager


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()  # type:ignore

    username = None  # type: ignore
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(
        _("Phone number"), max_length=150, blank=True, null=True
    )
    description = models.CharField(max_length=255, null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
