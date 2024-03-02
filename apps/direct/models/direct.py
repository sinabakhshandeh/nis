from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.user.models import User


class DirectChat(models.Model):
    participants = models.ManyToManyField(
        User, related_name="direct_chats", verbose_name="Participants"
    )

    class Meta:
        verbose_name = "Direct Chat"
        verbose_name_plural = "Direct Chats"

    def __str__(self):
        return ", ".join([str(user) for user in self.participants.all()])
