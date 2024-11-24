from sys import prefix

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api import Author
from api.authors.dependencies import get_author_id, get_author
from api.products.crud import create_product
from api.products.schemas import ProductBase
from api.users.dependencies import get_current_user_id
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