from .users.views import router as users_router

from fastapi import APIRouter

router = APIRouter()

router.include_router(users_router)