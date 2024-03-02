import logging
from typing import List

from ninja import Router

from apps.direct import services

from . import schemas

logger = logging.getLogger(__name__)
direct_router = Router()


@direct_router.get(
    "/{username}",
    response={200: schemas.DirectChatSchema, 401: schemas.ErrorSchema},
)
def direct_message_list(request, username: str):
    user_sub = request.auth["sub"]
    direct_messages = services.direct_message_list(
        user_uuid=user_sub,
        username=username,
    )
    return direct_messages


@direct_router.post(
    "/",
    response={200: schemas.DirectMessageSchema, 401: schemas.ErrorSchema},
)
def send_direct(
    request,
    direct_message_data: schemas.SendDirectMessageSchema,
):
    user_sub = request.auth["sub"]
    direct_message = services.send_direct(
        sender_uuid=user_sub,
        user_data=direct_message_data.dict(),
    )
    return direct_message
