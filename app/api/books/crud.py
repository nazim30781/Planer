from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api import Book


async def create_book(
        user_id: int,
        product_id: int,
        time_id: int,
        session: AsyncSession
):
    book = Book(product_id=product_id, user_id=user_id, time_id=time_id)

    session.add(book)

    await session.commit()
