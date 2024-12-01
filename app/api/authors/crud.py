from datetime import date

from dulwich.porcelain import reset
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from api import AuthorTable, AuthorTableDate
from api.authors.models import Author
from api.authors.schemas import AuthorBase, Table, Date, TableUpdate


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
        author_id: int,
        dates_data: list[date],
        session: AsyncSession
):
    dates = []

    query = select(AuthorTable).where(AuthorTable.id==table_id)

    auth = await session.execute(query)

    id = auth.first()[0].author_id

    print(id == author_id)

    if id == author_id:
        for data in dates_data:
            instance = AuthorTableDate(date=data)
            instance.table_id = table_id
            dates.append(instance)

        session.add_all(dates)
        await session.commit()
        return "success"

    return "you are not author"


async def get_first_author_table(
        author_id: int,
        session: AsyncSession
):
    query = select(Author).options(joinedload(Author.tables).joinedload(AuthorTable.dates)).where(Author.id==author_id)
    result = await session.execute(query)

    return result.first()[0]


async def get_author_details(
        author_id: int,
        session: AsyncSession
):
    query = (select(Author).
             options(joinedload(Author.products),
                     joinedload(Author.tables)
                     .joinedload(AuthorTable.dates))
             .where(Author.id==author_id))

    result = await session.execute(query)

    return result.first()[0]


async def get_all_author_tables(
        author_id: int,
        session: AsyncSession
):
    query = select(AuthorTable).options(joinedload(AuthorTable.dates)).filter(author_id==author_id)
    result = await session.execute(query)

    tables = result.unique().scalars().all()

    return tables


async def update_table_data(
        data: TableUpdate,
        author_id: int,
        session: AsyncSession
):
    query = select(AuthorTable).options(joinedload(AuthorTable.author), joinedload(AuthorTable.dates)).where(AuthorTable.id==data.table_id)

    result = await session.execute(query)
    table = result.first()[0]

    id = table.author.id

    if author_id == id:
        table.title = data.title
        table.min_hour = data.min_hour
        table.max_hour = data.max_hour

        dates = table.dates

        await delete_dates_from_table(data.table_id, session)
        await create_table_dates(data.table_id, author_id, data.dates, session)

        await session.commit()

async def delete_dates_from_table(table_id: int, session: AsyncSession):
    await session.execute(delete(AuthorTableDate).filter(table_id==table_id))
    await session.commit()
