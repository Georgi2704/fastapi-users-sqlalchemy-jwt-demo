from fastapi import Depends, FastAPI, APIRouter
from app.users import current_active_user, fastapi_users, cookie_authentication

api_router = APIRouter()

api_router.include_router(
    fastapi_users.get_auth_router(cookie_authentication), prefix="/auth/cookie", tags=["auth"]
)
api_router.include_router(
    fastapi_users.get_register_router(), prefix="/auth", tags=["auth"]
)
api_router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
api_router.include_router(
    fastapi_users.get_verify_router(),
    prefix="/auth",
    tags=["auth"],
)
api_router.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])
