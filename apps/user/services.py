import logging
from typing import Dict, cast

from asgiref.sync import sync_to_async
from django.db.utils import IntegrityError
from django.utils.translation import gettext_lazy as _
from ninja.errors import HttpError

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
        "username": user.username,
    }
    jwt_token = JWTToken()
    tokens = jwt_token.issue_tokens(sub=str(user.uuid), data=payload)

    user = cast(User, user)
    user = await User.objects.login(user)
    return tokens
