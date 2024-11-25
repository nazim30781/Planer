from typing import TYPE_CHECKING
from datetime import time, date

from sqlalchemy import Column, ForeignKey, Integer, Date, Time
from sqlalchemy.orm import Mapped, relationship

from core.models import Base

if TYPE_CHECKING:
    from api.users.models import User
    from api.products.models import Product


class Book(Base):
    product_id: int = Column(Integer, ForeignKey("product.id"), nullable=False)
    user_id: int = Column(Integer, ForeignKey("user.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="books")
    product: Mapped["Product"] = relationship(back_populates="books")


class BookDate(Base):
    book_id: int = Column(Integer, ForeignKey("book.id"), nullable=False)
    date: date = Column(Date, nullable=False)

    # book: Mapped["Book"] = relationship(back_populates="book_date")


class BookTime(Base):
    date_id: int = Column(Integer, ForeignKey("bookdate.id"), nullable=False)
    time: time = Column(Time, nullable=False)

    # date: Mapped["BookDate"] = relationship(back_populates="book_time")