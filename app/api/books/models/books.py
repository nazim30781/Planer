from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from core.models import Base

if TYPE_CHECKING:
    from api.users.models import User
    from api.products.products import Product
    from api.products.product_times import ProductTime


class Book(Base):
    product_id: int = Column(Integer, ForeignKey("product.id"), nullable=False)
    user_id: int = Column(Integer, ForeignKey("user.id"), nullable=False)
    time_id: int = Column(Integer, ForeignKey("producttime.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="books")
    product: Mapped["Product"] = relationship(back_populates="books")
    time: Mapped["ProductTime"] = relationship(back_populates="book")

    def __str__(self):
        return f"book - {self.id} of - {self.product_id} by - {self.user_id}"