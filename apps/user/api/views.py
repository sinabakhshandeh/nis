import logging
from uuid import UUID

from django.utils.translation import gettext_lazy as _
from ninja import Router

from apps.user import services

from . import schemas

logger = logging.getLogger(__name__)

router = Router()


# @router.post(
#     "/sample/",
#     response={200: schemas.SampleSchema, 401: schemas.ErrorSchema},
#     auth=None,
# )
# async def sample(request, sample: schemas.SampleSchema):
#     return sample


@router.post(
    "/register/",
    response={200: schemas.RegisterResponseSchema, 401: schemas.ErrorSchema},
    auth=None,
)
async def register(request, user_data: schemas.UserRegistrationSChema):
    tokens = await services.sign_up(user_data=user_data.dict())
    return tokens


@router.post(
    "/login/",
    response={200: schemas.LoginResponseSchema, 401: schemas.ErrorSchema},
    auth=None,
)
async def login(request, user_data: schemas.UserLoginSchema):
    token = await services.login(user_data=user_data.dict())
    return token


@router.get(
    "/users/profile/{username}/",
    response={200: schemas.ProfileSchema, 401: schemas.ErrorSchema},
)
def user_profile(request, username: str):
    user_sub = request.auth["sub"]
    user = services.user_profile(username=username, user_sub=user_sub)
    return user


@router.patch(
    "/users/{id}/",
    response={200: schemas.UserSchema, 401: schemas.ErrorSchema},
    auth=None,
)
def update_user(request, id: UUID, user_data: schemas.UpdateSchema):
    user_sub = request.auth["sub"]
    user = services.update_user(
        sub=user_sub, current_user=id, data=user_data.dict(exclude_none=True)
    )
    return user
