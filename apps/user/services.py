import logging
from typing import Dict, cast
from uuid import UUID

from asgiref.sync import sync_to_async
from django.contrib.auth import authenticate
from django.db.utils import IntegrityError
from django.utils.translation import gettext_lazy as _
from ninja.errors import HttpError

from apps.log.models import ProfileViewLog
from apps.user.jwt_handler import JWTToken
from apps.user.models import User

logger = logging.getLogger(__name__)


async def sign_up(user_data: Dict[str, str]) -> Dict[str, str]:
    password = user_data.pop("password")
    email = user_data.pop("email")

    try:
        user = await sync_to_async(
            User.objects.create_user, thread_sensitive=True
        )(email, password, **user_data)
    except IntegrityError as e:
        logger.debug(f"user with email {email} alredye exists {e}")
        raise HttpError(400, "User with this email already exists")

    payload = {
        "name": f"{user.first_name} {user.last_name}",
        "admin  ": user.is_superuser,
    }
    jwt_token = JWTToken()
    tokens = jwt_token.issue_tokens(sub=str(user.uuid), data=payload)

    user = cast(User, user)
    user = await User.objects.login(user)
    return tokens


async def login(*, user_data: Dict[str, str]) -> Dict[str, str]:
    email = user_data["email"]
    password = user_data["password"]
    user = await sync_to_async(authenticate, thread_sensitive=True)(
        email=email, password=password
    )
    user = cast(User, user)
    if user is None:
        raise HttpError(401, "Password is not correct or user not exists.")

    payload = {
        "name": f"{user.first_name} {user.last_name}",
        "admin": user.is_superuser,
    }
    jwt_token = JWTToken()
    tokens = jwt_token.issue_tokens(sub=str(user.uuid), data=payload)
    user = await User.objects.login(cast(User, user))
    return tokens


def update_user(*, current_user: UUID, sub: UUID, data: dict) -> User:
    if str(current_user) != str(sub):
        raise HttpError(403, "You don't have enough permissions for this API")

    user = User.objects.filter(uuid=sub)
    if not user.exists():
        raise HttpError(404, "Not Found: No User matches the given query.")

    password = data.get("password")
    if password:
        password = data.pop("password")

    try:
        user.update(**data)
    except IntegrityError as e:
        logger.exception(e)
        raise HttpError(400, "User already exists")

    user_obj = user[0]
    if password:
        user_obj.set_password(password)
        user_obj.save()

    user_obj.refresh_from_db()
    return user_obj


def user_profile(username: str, user_sub: UUID) -> User:
    user = User.objects.filter(username=username)
    viewer = User.objects.filter(uuid=user_sub).first()
    if not user.exists():
        raise HttpError(404, "Not Found: No User matches the given query.")
    ProfileViewLog.objects.create(
        viewer=viewer,
        viewed_profile=user.first(),
    )
    return user
