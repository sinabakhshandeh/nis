from django.db import models
from django.utils import timezone

from apps.user.models import User


class ProfileViewLog(models.Model):
    viewer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="viewed_profiles",
        verbose_name="Viewer",
    )
    viewed_profile = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="profile_views",
        verbose_name="Viewed Profile",
    )
    viewed_at = models.DateTimeField(
        default=timezone.now, verbose_name="Viewed At"
    )

    class Meta:
        verbose_name = "Profile View Log"
        verbose_name_plural = "Profile View Logs"

    def __str__(self):
        return f"{self.viewer.username} viewed\
            {self.viewed_profile.username}'s profile on {self.viewed_at}"
