from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.authors.dependencies import get_author_id
from api.products.schemas import ProductBase

from .models import Product


async def create_product(
        product_data: ProductBase,
        session: AsyncSession,
        author_id: int
):
    new_product = Product(**product_data.model_dump())
    new_product.author_id = author_id

    session.add(new_product)
    await session.commit()

    return new_product