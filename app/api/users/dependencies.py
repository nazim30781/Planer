from fastapi import Request
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials

from .utils import decode_token


class AccessTokenBearer(HTTPBearer):
    def __init__(self, auto_error = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        creds = await super().__call__(request)

        token = creds.credentials

        token_data = decode_token(token)

        if not self.token_valid:
            raise "Validation Error"

        if token_data['refresh']:
            raise "Refresh Error"

        return creds

    def token_valid(self, token: str) -> bool:
        token_data = decode_token(token)

        if token_data is not None:
            return True

        return False
