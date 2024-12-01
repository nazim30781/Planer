from datetime import time, datetime, date
from itertools import product

from fastapi.params import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from api.products.schemas import ProductBase

from .products import Product
from .. import AuthorTable, ProductTime, ProductDate, Author
from ..authors.crud import get_first_author_table
from ..authors.dependencies import get_author_with_products, get_author_id


async def create_product(
        product_data: ProductBase,
        session: AsyncSession,
        author_id: int
):
    new_product = Product(**product_data.model_dump())
    new_product.author_id = author_id

    session.add(new_product)
    await session.flush()

    await create_days_for_product(new_product.id, author_id, session)

    return new_product


async def create_days_for_product(
        product_id,
        author_id: int,
        session: AsyncSession,
        dates: list[date] | None,
):
    result = await get_first_author_table(author_id, session)
    author_table = result.tables[0]

    if dates is None:
        query = select(Product).where(Product.id == product_id)

        product = await session.execute(query)

        hours = product.first()[0].hours

        dates = author_table.dates

    for date in dates:
        instance = ProductDate(date=date.date, product_id=product_id)

        session.add(instance)

        await session.flush()

        await create_times_for_date(
            instance.id,
            author_table.min_hour,
            author_table.max_hour,
            hours,
            session
        )

    await session.commit()


async def create_times_for_date(
        date_id: int,
        min_hour: int,
        max_hour: int,
        product_hours: int,
        session: AsyncSession
):
    print(product_hours)
    times = []

    for i in range(min_hour, max_hour + 1, product_hours):
        c_time = time(i, 0, 0)
        new_time = ProductTime(time=c_time)
        new_time.date_id = date_id

        times.append(new_time)
        session.add(new_time)


async def get_product(
        product_id: int,
        session: AsyncSession
):
    query = (select(Product).
             options(joinedload(Product.dates).
                     joinedload(ProductDate.times)).
             where(Product.id==product_id))

    result = await session.execute(query)
    product = result.first()[0]

    return product


async def get_all_products(
        session: AsyncSession
):
    query = select(Product)

    products = await session.execute(query)


    return products.scalars().all()


async def get_product_time_id(
        product_id: int,
        product_time: datetime,
        session: AsyncSession
):
    query = select(Product).options(joinedload(Product.dates).joinedload(ProductDate.times)).where(Product.id==product_id)

    product = await session.execute(query)
    product = product.first()[0]

    for date in product.dates:
        if date.date.date()==product_time.date():
            for time in date.times:
                if time.time.hour == product_time.time().hour and time.time.minute == product_time.time().minute:
                    return time.id


async def add_days_for_product(
        product_id: int,
        dates: list[date],
        author_id: int,
        session: AsyncSession,
):
    await create_days_for_product(product_id, author_id, session, dates)