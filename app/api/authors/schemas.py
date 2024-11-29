from datetime import date

from pydantic import BaseModel


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