from datetime import datetime

from fastapi import APIRouter
from fastapi.params import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from .crud import create_book, get_product_books

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


@router.get("/get_product_books")
async def get_product_books_view(
        product_id: int,
        session: AsyncSession = Depends(db_helper.session_getter)
):
    return await get_product_books(product_id, session)