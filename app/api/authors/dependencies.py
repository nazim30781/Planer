from fastapi.params import Depends

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.dependencies import access_token_bearer
from api.users.models import User
from core.models import db_helper


async def get_author(
        session: AsyncSession = Depends(db_helper.session_getter),
        user_data: dict = Depends(access_token_bearer)
):
    print(user_data["user_details"]["id"])
    query = (select(User)
             .options(joinedload(User.author))
             .where(User.id == user_data["user_details"]["id"]))

    author = await session.execute(query)

    print(author.first()[0].author.username)

    return author
