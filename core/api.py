from ninja import NinjaAPI

from apps.user.api.views import router as user_router

from .middlewares import AuthBearer, BasicAuth

api = NinjaAPI(auth=[AuthBearer(), BasicAuth()])

api.add_router("/auth/", user_router, tags=["Auth"])
