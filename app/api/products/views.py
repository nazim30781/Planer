from datetime import datetime, date

from fastapi import APIRouter
from fastapi.params import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from api import Author
from api.authors.dependencies import get_author_id, get_author, get_author_with_products
from api.products.crud import create_product, create_days_for_product, get_product, get_product_time_id, \
    get_all_products, add_days_for_product
from api.products.schemas import ProductBase, ProductDateTimeCreate, ProductData

from core.config import settings
from core.models import db_helper

router = APIRouter(
    prefix=settings.api.apps.products,
    tags=["Products"]
)


@router.post("/create_product")
async def create_product_view(
        product_data: ProductBase,
        session: AsyncSession = Depends(db_helper.session_getter),
        author_id: int = Depends(get_author_id)
):
    new_product = await create_product(product_data, session, author_id)

    return new_product


@router.post("/create_dates_and_times")
async def create_dates_and_times(
        product_id: int,
        author_id: int = Depends(get_author_id),
        session: AsyncSession = Depends(db_helper.session_getter)
):
    await create_days_for_product(product_id, author_id, session)
    return "success"


@router.get("/get_product")
async def get_product_view(
        product_id: int,
        session: AsyncSession = Depends(db_helper.session_getter)
):
    return await get_product(product_id, session)


@router.get("/get_all_products")
async def get_all_products_view(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    return await get_all_products(session)


@router.post("/add_days_for_product")
async def add_days_for_product_view(
        product_id: int,
        dates: list[date],
        author_id: int = Depends(get_author_id),
        session: AsyncSession = Depends(db_helper.session_getter)
):
    await add_days_for_product(product_id, dates, author_id, session)
