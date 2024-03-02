import logging
from functools import wraps

import jwt
from django.contrib.auth import authenticate
from ninja.errors import HttpError
from ninja.security import HttpBasicAuth, HttpBearer

from apps.user.jwt_handler import JWTToken

logger = logging.getLogger(__name__)


class AuthBearer(HttpBearer):
    """
    Decode the auth token and will put in `request.auth`
    """

    def authenticate(self, request, token):
        if token:
            try:
                decoded_token = JWTToken.decode(token)
                return decoded_token
            except jwt.exceptions.DecodeError:
                logger.debug(f"Auth: decode error with token {token}")
        return None


class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, email, password):
        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                return None
            return {
                "name": user.first_name,
                "admin": user.is_superuser,
                "sub": user.uuid,
            }


def optional_auth(request):
    basic = BasicAuth()
    basic_auth = basic(request)
    bearer = AuthBearer()
    bearer_auth = bearer(request)
    if bearer_auth:
        return bearer_auth
    elif basic_auth:
        return basic_auth
    return None
