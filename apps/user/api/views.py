import logging

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
