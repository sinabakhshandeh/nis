from datetime import datetime
from typing import List, Literal, Optional

from ninja import Schema

from apps.user.api.schemas import ProfileSchema

FileType = Literal["voice", "image", "video", ""]


class ErrorSchema(Schema):
    message: str


class DirectMessageSchema(Schema):
    file: Optional[str]
    file_type: Optional[FileType]
    text: Optional[str]
    send_to: str


class SendDirectMessageSchema(DirectMessageSchema):
    pass


class MessageContentSchema(Schema):
    id: int
    text: str
    file: str
    file_type: str
    is_text: bool


class Message(Schema):
    sender: ProfileSchema
    sent_at: datetime
    content: MessageContentSchema


class DirectChatSchema(Schema):
    participants: List[ProfileSchema]
    messages: List[Message]
