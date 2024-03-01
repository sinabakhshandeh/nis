from ninja import NinjaAPI

from apps.user.api.views import router as user_router


api = NinjaAPI()

api.add_router("/auth/", user_router, tags=["Auth"])
