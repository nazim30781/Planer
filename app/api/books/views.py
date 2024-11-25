from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper

from .schemas import BookBase
from ..users.dependencies import get_current_user_id

router = APIRouter(
    prefix=settings.api.apps.books,
    tags=["Books"]
)

@router.post("/create_book")
async def create_book_view(
        book_data: BookBase,
        user_id: int = Depends(get_current_user_id),
        session: AsyncSession = Depends(db_helper.session_getter)
):

    print(book_data.time.hour)

    return user_id