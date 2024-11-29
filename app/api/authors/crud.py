from datetime import date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from api import AuthorTable, AuthorTableDate
from api.authors.models import Author
from api.authors.schemas import AuthorBase, Table, Date


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


async def create_table(
        author_id: int,
        table: Table,
        session: AsyncSession
):
    new_table = AuthorTable(**table.model_dump())
    new_table.author_id = author_id

    session.add(new_table)
    await session.commit()

    return new_table


async def create_table_dates(
        table_id: int,
        dates_data: list[date],
        session: AsyncSession
):
    dates = []
    for data in dates_data:
        print(data)
        instance = AuthorTableDate(date=data)
        instance.table_id = table_id
        dates.append(instance)

    session.add_all(dates)
    await session.commit()


async def get_first_author_table(
        author_id: int,
        session: AsyncSession
):
    query = select(Author).options(joinedload(Author.tables).joinedload(AuthorTable.dates)).where(Author.id==author_id)
    result = await session.execute(query)


    return result.first()[0]