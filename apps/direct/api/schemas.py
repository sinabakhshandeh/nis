from typing import Literal, Optional

from ninja import Schema

FileType = Literal["voice", "image", "video", ""]


class ErrorSchema(Schema):
    message: str


class DirectMessageSchema(Schema):
    file: Optional[str]
    file_type: Optional[FileType]
    text: Optional[str]
    receiver: str


class SendDirectMessageSchema(DirectMessageSchema):
    pass
