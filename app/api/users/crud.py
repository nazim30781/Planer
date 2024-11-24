from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User
from .schemas import UserCreateModel
from .utils import generate_passwd_hash


async def get_user_by_email(
        email:str,
        session: AsyncSession
):
    query = select(User).where(User.email == email)

    result = await session.execute(query)
    user = result.first()

    if user:
        return user[0]

    return None

async def user_exists(
        email: str,
        session: AsyncSession
) -> User | None:
    user = await get_user_by_email(email, session)

    if user is not None:
        return user

    return None

async def create_user(
        user_data: UserCreateModel,
        session: AsyncSession
) -> User:
    new_user = User(**user_data.model_dump())
    new_user.password = generate_passwd_hash(new_user.password)

    session.add(new_user)
    await session.commit()

    return new_user


