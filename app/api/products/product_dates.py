from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Column, TIMESTAMP, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from core.models import Base

if TYPE_CHECKING:
    from .products import Product
    from .product_times import ProductTime


class ProductDate(Base):
    date: date = Column(TIMESTAMP, nullable=False)
    product_id: int = Column(Integer, ForeignKey("product.id"), nullable=False)

    product: Mapped["Product"] = relationship(back_populates="dates")
    times: Mapped[list["ProductTime"]] = relationship(back_populates="date")