from typing import TYPE_CHECKING
from datetime import datetime, date, time

from sqlalchemy import Column, String, TIMESTAMP, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from core.models import Base

if TYPE_CHECKING:
    from api.authors.models import Author
    from api.books.models import Book
    from .product_dates import ProductDate


class Product(Base):
    title: str = Column(String, nullable=False)
    description: str = Column(String, nullable=True)
    created_at: datetime = Column(TIMESTAMP, default=datetime.now)
    author_id: int = Column(Integer, ForeignKey("author.id"), nullable=False)
    hours: int = Column(Integer, default=1)

    author: Mapped["Author"] = relationship(back_populates="products")
    books: Mapped[list["Book"]] = relationship(back_populates="product")
    dates: Mapped[list["ProductDate"]] = relationship(back_populates="product")
