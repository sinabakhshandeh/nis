from typing import Dict
from uuid import UUID

from django.contrib.contenttypes.models import ContentType

from apps.direct import models
from apps.user.models import User


def send_direct(
    sender_uuid=UUID,
    user_data=Dict,
):
    sender_obj = User.objects.filter(uuid=sender_uuid).first()
    receiver = user_data.get("receiver")
    receiver_obj = User.objects.filter(username=receiver).first()
    text = user_data.get("text", None)
    file = user_data.get("file", None)
    direct_chats = models.DirectChat.objects.filter(
        participants=sender_obj
    ).filter(participants=receiver_obj)

    if direct_chats.exists():
        direct_chat = direct_chats.first()
    else:
        direct_chat = models.DirectChat.objects.create()
        direct_chat.participants.add(sender_obj)
        direct_chat.participants.add(receiver_obj)

    if text:
        direct_message = models.DirectMessage.objects.create(
            sender=sender_obj,
            chat=direct_chat,
        )
        text_obj = models.Text.objects.create(text=text)
        models.DirectMessageContent.objects.create(
            message=direct_message,
            content_object=text_obj,
        )
    if file:
        direct_message = models.DirectMessage.objects.create(
            sender=sender_obj,
            chat=direct_chat,
        )
        file_type = user_data.get("file_type")
        file_obj = models.Media.objects.create(file=file, file_type=file_type)
        models.DirectMessageContent.objects.create(
            message=direct_message,
            content_object=file_obj,
        )
    return user_data
