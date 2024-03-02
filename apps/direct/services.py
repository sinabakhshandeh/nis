from typing import Dict
from uuid import UUID

from django.shortcuts import get_object_or_404
from ninja.errors import HttpError

from apps.direct import models
from apps.user.models import User


def send_direct(
    sender_uuid=UUID,
    user_data=Dict,
):
    sender_obj = User.objects.filter(uuid=sender_uuid).first()
    receiver = user_data.get("send_to")
    receivers = User.objects.filter(username=receiver)
    if not receivers.exists():
        raise HttpError(404, "Not Found: No User matches the given query.")
    receiver_obj = receivers.first()
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


def direct_message_list(user_uuid: UUID, username: str):
    user = User.objects.get(uuid=user_uuid)
    target = get_object_or_404(User, username=username)
    direct_chat = (
        models.DirectChat.objects.filter(participants=user)
        .filter(participants=target)
        .first()
    )

    messages = models.DirectMessage.objects.filter(chat=direct_chat)
    chat_messages = []
    for m in messages:
        content = models.DirectMessageContent.objects.get(message=m)
        text = ""
        file = ""
        file_type = ""
        is_text = False
        if isinstance(content.content_object, models.Text):
            text = content.content_object.text
            is_text = True
        else:
            file = content.content_object.file
            file_type = content.content_object.file_type
        m.content = {
            "id": content.object_id,
            "is_text": is_text,
            "text": text,
            "file": file,
            "file_type": file_type,
        }
        chat_messages.append(m)
        print(content)
    return {
        "participants": [user, target],
        "messages": chat_messages,
    }
