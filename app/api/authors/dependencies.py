from fastapi.params import Depends

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.dependencies import access_token_bearer, get_current_user_id
from api.users.models import User
from core.models import db_helper


async def get_author_id(
        session: AsyncSession = Depends(db_helper.session_getter),
        user_id: dict = Depends(get_current_user_id)
):
    query = (select(User)
             .options(joinedload(User.author))
             .where(User.id == user_id))

    user = await session.execute(query)

    author_id = user.first()[0].author.id
    print(author_id)

    return author_id


async def get_author(
        session: AsyncSession = Depends(db_helper.session_getter),
        user_id: dict = Depends(get_current_user_id)
):
    query = (select(User)
             .options(joinedload(User.author))
             .where(User.id == user_id))

    user = await session.execute(query)

    author_id = user.first()[0].author

    return author_id
