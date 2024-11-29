from datetime import time
from typing import TYPE_CHECKING

from sqlalchemy import Column, TIMESTAMP, ForeignKey, Integer, Time
from sqlalchemy.orm import Mapped, relationship

from core.models import Base

if TYPE_CHECKING:
    from .product_dates import ProductDate
    from api.books.models.books import Book


class ProductTime(Base):
    time: time = Column(Time, nullable=False)
    date_id: int = Column(Integer, ForeignKey("productdate.id"), nullable=False)

    date: Mapped["ProductDate"] = relationship(back_populates="times")
    book: Mapped["Book"] = relationship(back_populates="time")