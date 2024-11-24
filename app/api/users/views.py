from datetime import timedelta

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper

from .schemas import UserCreateModel, UserBase
from .utils import verify_password, create_access_token
from .crud import user_exists, create_user, get_user_by_email


router = APIRouter(
    prefix=settings.api.apps.users,
    tags=["Users"]
)

REFRESH_TOKEN_EXPIRY = 2


@router.post("/signup")
async def create_user_account(user_data: UserCreateModel,
                              session: AsyncSession = Depends(db_helper.session_getter)):
    email = user_data.email

    user_exist = await user_exists(email, session)

    if user_exist:
        raise 'Error'

    new_user = await create_user(user_data, session)

    return new_user


@router.post('/login')
async def login_user(login_data: UserBase,
                     session: AsyncSession = Depends(db_helper.session_getter)):
    email = login_data.email
    password = login_data.password

    user = await get_user_by_email(email, session)
    user = user

    if user is not None:
        password_valid = verify_password(password, user.password)

        if password_valid:
            access_token = create_access_token(
                user_data={
                    'email': user.email,
                    'id': user.id
                }
            )

            refresh_token = create_access_token(
                user_data={
                    'email': user.email,
                    'id': user.id
                },
                refresh=True,
                expiry=timedelta(days=REFRESH_TOKEN_EXPIRY)
            )

            return JSONResponse(
                content={
                    "message": "Login successful",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "user": {
                        "email": user.email,
                        "id": str(user.id)
                    }
                }
            )

    raise "error"
