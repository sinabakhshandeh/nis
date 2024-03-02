from typing import Optional
from uuid import UUID

from ninja import ModelSchema, Schema
from pydantic import EmailStr

from apps.user.models import User


class ErrorSchema(Schema):
    message: str


class SampleSchema(Schema):
    name: str


class UserRegistrationSChema(Schema):
    email: EmailStr
    password: str
    username: str


class RefreshTokenSchema(Schema):
    refresh_token: str


class RegisterResponseSchema(RefreshTokenSchema):
    access_token: str


class EmailSchema(Schema):
    email: EmailStr


class UserLoginSchema(EmailSchema):
    password: str


class LoginResponseSchema(RefreshTokenSchema):
    access_token: str


class UpdateSchema(Schema):
    description: Optional[str]
    password: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    uuid: Optional[UUID]


class ProfileSchema(ModelSchema):
    class Config:
        model = User
        model_fields = [
            "first_name",
            "last_name",
            "date_joined",
            "description",
            "phone_number",
        ]


class UserSchema(ProfileSchema):
    email: EmailStr
