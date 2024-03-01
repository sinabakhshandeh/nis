import logging

from django.utils.translation import gettext_lazy as _
from ninja import Router

from . import schemas

logger = logging.getLogger(__name__)

router = Router()


@router.post(
    "/sample/",
    response={200: schemas.SampleSchema, 401: schemas.ErrorSchema},
    auth=None,
)
async def sample(request, sample: schemas.SampleSchema):
    return sample
