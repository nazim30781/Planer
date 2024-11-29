from datetime import date, time, datetime

from pydantic import BaseModel


class ProductBase(BaseModel):
    title: str
    description: str
    hours: int


class ProductDateTimeCreate(BaseModel):
    data: dict[date, time]


class ProductData(BaseModel):
    product_id: int
    date: datetime