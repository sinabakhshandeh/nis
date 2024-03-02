from datetime import datetime, timedelta
from typing import Dict

import jwt

from core import settings


class JWTToken:

    algorithm = "RS256"

    def encode(self, payload) -> str:
        return jwt.encode(
            payload, settings.PRIVATE_KEY, algorithm=self.algorithm
        )

    def issue_tokens(self, *, sub: str, data: dict) -> Dict[str, str]:

        access_token_payload = self.create_jwt_claims(
            sub=sub, data=data, refresh_token=False
        )
        refresh_token_payload = self.create_jwt_claims(
            sub=sub, data={}, refresh_token=True
        )
        access_token = self.encode(access_token_payload)
        refresh_token = self.encode(refresh_token_payload)
        return {"access_token": access_token, "refresh_token": refresh_token}

    def refresh_token(self, sub: str, data: dict) -> Dict[str, str]:
        access_token_payload = self.create_jwt_claims(
            sub=sub, data=data, refresh_token=False
        )
        access_token = self.encode(access_token_payload)
        return {"access_token": access_token}

    def create_jwt_claims(
        self, *, sub: str, data: dict, refresh_token: bool = False
    ):
        now = datetime.utcnow()
        duration = (
            timedelta(hours=72) if refresh_token else timedelta(minutes=180)
        )
        payload = {
            **data,
            "sub": sub,
            "iat": int(now.timestamp()),
            "exp": int((now + duration).timestamp()),
        }
        return payload

    @classmethod
    def decode(cls, token: str) -> Dict[str, str]:
        return jwt.decode(
            jwt=token,
            key=settings.PUBLIC_KEY,
            options={"require": ["exp", "iat"]},
            algorithms=[cls.algorithm],
        )
