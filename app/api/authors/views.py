from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.authors.crud import create_author
from api.authors.schemas import AuthorBase
from api.users.dependencies import access_token_bearer
from core.config import settings
from core.models import db_helper

router = APIRouter(
    prefix=settings.api.apps.authors,
    tags=["Authors"]
)

@router.post("/create_author")
async def create_author_view(
        author_data: AuthorBase,
        user: dict = Depends(access_token_bearer),
        session: AsyncSession = Depends(db_helper.session_getter)
):

    user_id = user["user_details"]["id"]

    author = await create_author(user_id, author_data, session)

    if author is not None:
        return author