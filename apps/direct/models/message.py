from datetime import datetime

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.user.models import User

from .direct import DirectChat


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


def direct_message_upload_path(instance, filename):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"direct_messages/{instance.message.chat.id}/{timestamp}-{filename}"


class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = "image", _("IMAGE")
        VIDEO = "video", _("VIDEO")
        VOICE = "voice", _("VOICE")

    file = models.FileField(upload_to=direct_message_upload_path)

    file_type = models.CharField(
        max_length=25,
        choices=FileType.choices,
        default=FileType.IMAGE,
        help_text=_("Project current status"),
    )


class Text(models.Model):
    text = models.CharField()


class DirectMessageContent(models.Model):
    message = models.ForeignKey(
        DirectMessage,
        on_delete=models.CASCADE,
        related_name="contents",
        verbose_name="Message",
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name="Content Type",
    )
    object_id = models.PositiveIntegerField(verbose_name="Object ID")
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        verbose_name = "Direct Message Content"
        verbose_name_plural = "Direct Message Contents"
