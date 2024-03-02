from ninja import NinjaAPI

from apps.direct.api.views import direct_router
from apps.user.api.views import auth_router, profile_router

from .middlewares import AuthBearer, BasicAuth

api = NinjaAPI(auth=[AuthBearer(), BasicAuth()])

api.add_router("/auth/", auth_router, tags=["Auth"])
api.add_router("/profiles/", profile_router, tags=["Profile"])
api.add_router("/directs/", direct_router, tags=["Direct"])
