from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import Column, String, TIMESTAMP, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from core.models import Base

if TYPE_CHECKING:
    from api.authors.models import Author


class Product(Base):
    title: str = Column(String, nullable=False)
    description: str = Column(String, nullable=True)
    created_at: datetime = Column(TIMESTAMP, default=datetime.now)
    author_id: int = Column(Integer, ForeignKey("author.id"), nullable=False)

    # author: Mapped["Author"] = relationship(back_populates="products")
