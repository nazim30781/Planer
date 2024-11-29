from typing import TYPE_CHECKING

from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from core.models import Base

if TYPE_CHECKING:
    from .author_table_date import AuthorTableDate
    from .models import Author


class AuthorTable(Base):
    table_title: str = Column(String)
    min_hour: int = Column(Integer)
    max_hour: int = Column(Integer)
    author_id: int = Column(Integer, ForeignKey("author.id"))

    dates: Mapped[list["AuthorTableDate"]] = relationship(back_populates="table")
    author: Mapped["Author"] = relationship(back_populates="tables")