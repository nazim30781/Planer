from pydantic import BaseModel


class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    username: str