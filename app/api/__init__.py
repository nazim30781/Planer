from core.config import settings
from .users.views import router as users_router

from fastapi import APIRouter

router = APIRouter(
    prefix=settings.api.prefix
)

router.include_router(users_router)