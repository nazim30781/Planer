from sqlalchemy.ext.asyncio import AsyncSession

from api.authors.models import Author
from api.authors.schemas import AuthorBase


async def create_author(
        user_id: int,
        author_data: AuthorBase,
        session: AsyncSession,
) -> Author:
    new_author = Author(**author_data.model_dump())
    new_author.user_id = user_id

    session.add(new_author)
    await session.commit()

    return new_author