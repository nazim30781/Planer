from datetime import datetime

from fastapi import APIRouter
from fastapi.params import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from .crud import create_book

from .schemas import BookBase
from ..products.crud import get_product_time_id
from ..products.schemas import ProductData
from ..users.dependencies import get_current_user_id

router = APIRouter(
    prefix=settings.api.apps.books,
    tags=["Books"]
)


@router.post("/create_book")
async def create_book_view(
        data: ProductData,
        user_id: int = Depends(get_current_user_id),
        session: AsyncSession = Depends(db_helper.session_getter)
):

    time_id = await get_product_time_id(data.product_id, data.date, session)

    await create_book(user_id, data.product_id, time_id, session)