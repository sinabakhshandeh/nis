from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

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


class DirectMessage(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_messages",
        verbose_name="Sender",
    )
    chat = models.ForeignKey(
        DirectChat,
        on_delete=models.CASCADE,
        related_name="messages",
        verbose_name="Chat",
    )
    content = models.TextField(verbose_name="Content")
    sent_at = models.DateTimeField(
        default=timezone.now, verbose_name="Sent At"
    )

    class Meta:
        ordering = ["sent_at"]
        verbose_name = "Direct Message"
        verbose_name_plural = "Direct Messages"

    def __str__(self):
        return f"Message from {self.sender.username} at {self.sent_at}"

    def clean(self):
        if self.participants.count() != 2:
            raise ValidationError(
                "A direct chat must have exactly two participants.",
            )
