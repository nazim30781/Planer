from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.authors.crud import create_author
from api.authors.schemas import AuthorBase
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