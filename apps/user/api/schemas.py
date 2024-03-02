from ninja import Schema
from pydantic import EmailStr


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
