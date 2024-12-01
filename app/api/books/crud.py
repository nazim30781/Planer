from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from api import Book, Product, ProductDate


async def create_book(
        user_id: int,
        product_id: int,
        time_id: int,
        session: AsyncSession
):
    book = Book(product_id=product_id, user_id=user_id, time_id=time_id)

    session.add(book)

    await session.commit()


async def get_product_books(
        product_id: int,
        session: AsyncSession
):
    query = select(Product).options(joinedload(Product.books).joinedload(Book.time), joinedload(Product.dates)).where(Product.id==product_id)

    result = await session.execute(query)

    return result.first()[0]