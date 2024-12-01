from datetime import date

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.util import await_only

from api import User
from api.authors.crud import create_author, create_table, create_table_dates, get_author_details, \
    get_first_author_table, get_all_author_tables, update_table_data
from api.authors.dependencies import get_author_id
from api.authors.schemas import AuthorBase, Table, Date, TableUpdate
from api.users.dependencies import get_current_user_id
from core.config import settings
from core.models import db_helper

router = APIRouter(
    prefix=settings.api.apps.authors,
    tags=["Authors"]
)

@router.post("/create_author")
async def create_author_view(
        author_data: AuthorBase,
        user_id: int = Depends(get_current_user_id),
        session: AsyncSession = Depends(db_helper.session_getter)
):

    author = await create_author(user_id, author_data, session)

    if author is not None:
        return author


@router.post("/create_author_table")
async def create_author_table_view(
        table_data: Table,
        author_id: int = Depends(get_author_id),
        session: AsyncSession = Depends(db_helper.session_getter)
):
    await create_table(author_id, table_data, session)

    return "success"


@router.post("/create_dates_for_table")
async def create_dates_for_table_view(
        table_id: int,
        dates_data: list[date],
        author_id: int = Depends(get_author_id),
        session: AsyncSession = Depends(db_helper.session_getter)
):
    response = await create_table_dates(table_id, author_id, dates_data, session)

    return response


@router.get("/get_author_details")
async def get_author_details_view(
        author_id: int,
        session: AsyncSession = Depends(db_helper.session_getter)
):
    return await get_author_details(author_id, session)


@router.get("/get_first_table")
async def get_first_table_view(
        author_id: int,
        session: AsyncSession = Depends(db_helper.session_getter)
):
    return await get_first_author_table(author_id, session)


@router.get("/get_all_author_tables")
async def get_all_author_tables_view(
        author_id: int,
        session: AsyncSession = Depends(db_helper.session_getter)
):
    return await get_all_author_tables(author_id, session)


@router.post("update_table")
async def update_table_view(
        data: TableUpdate,
        author_id: int = Depends(get_author_id),
        session: AsyncSession = Depends(db_helper.session_getter)
):
    await update_table_data(data, author_id, session)