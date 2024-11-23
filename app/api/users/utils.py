import datetime
from datetime import timedelta

from passlib.context import CryptContext

import jwt

from core.config import settings


ACCESS_TOKEN_EXPIRY = 3600


passwd_context = CryptContext(
    schemes=['bcrypt']
)


def generate_passwd_hash(password: str) -> str:
    hash = passwd_context.hash(password)

    return hash


def verify_password(password: str, hash: str) -> bool:
    return passwd_context.verify(password, hash)


def create_access_token(user_data: dict, expiry: timedelta = None, refresh: bool = False):
    payload = dict()

    payload['user'] = user_data
    payload['exp'] = (datetime.datetime.now() +
                      (expiry if expiry is not None else timedelta(seconds=ACCESS_TOKEN_EXPIRY)))
    payload['refresh'] = refresh

    token = jwt.encode(
        payload=payload,
        key=settings.jwt.jwt_secret,
        algorithm=settings.jwt.jwt_algorithm
    )

    return token


def decode_token(token: str) -> dict:
    try:
        token_data = jwt.decode(
            jwt=token,
            key=settings.jwt.jwt_secret,
            algorithms=[settings.jwt.jwt_algorithm]
        )

        return token_data

    except jwt.PyJWTError as error:
        print(error)