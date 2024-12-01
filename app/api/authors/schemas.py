from datetime import date

from pydantic import BaseModel
from virtualenv.config.convert import NoneType


class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    username: str


class Table(BaseModel):
    table_title: str
    min_hour: int
    max_hour: int


class Date(BaseModel):
    data: list[date]


class TableUpdate(BaseModel):
    table_id: int
    title: str | None
    min_hour: int | None
    max_hour: int | None
    dates: list[date]