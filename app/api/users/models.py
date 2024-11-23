from typing import TYPE_CHECKING

from datetime import datetime

from sqlalchemy import Column, String, Boolean, TIMESTAMP
from sqlalchemy.orm import Mapped, relationship

from core.models import Base

if TYPE_CHECKING:
    from api.authors.models import Author


class User(Base):
    email: str = Column(String, nullable=False, unique=True)
    password: str = Column(String, nullable=False)
    is_verify: str = Column(Boolean, default=False)
    created_at: datetime = Column(TIMESTAMP, default=datetime.now)

    author: Mapped["Author"] = relationship(back_populates="user")