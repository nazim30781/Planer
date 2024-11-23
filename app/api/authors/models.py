from typing import TYPE_CHECKING

from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship, Mapped

from api.users.models import User
from core.models import Base

if TYPE_CHECKING:
    from api.users.models import User


class Author(Base):
    username: str = Column(String, nullable=False, unique=True)
    first_name: str = Column(String, nullable=False)
    last_name: str = Column(String, nullable=True)
    user_id: int = Column(Integer, ForeignKey("user.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="author")