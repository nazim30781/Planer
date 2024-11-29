from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Column, TIMESTAMP, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from core.models import Base

if TYPE_CHECKING:
    from .author_table import AuthorTable


class AuthorTableDate(Base):
    date: date = Column(TIMESTAMP, nullable=False)
    min_hour: int = Column(Integer)
    max_hour: int = Column(Integer)
    table_id: int = Column(Integer, ForeignKey("authortable.id"))

    table: Mapped["AuthorTable"] = relationship(back_populates="dates")