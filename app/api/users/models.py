from datetime import datetime

from sqlalchemy import Column, String, Boolean, TIMESTAMP

from core.models import Base


class User(Base):
    email: str = Column(String, nullable=False, unique=True)
    username: str = Column(String, nullable=False, unique=True)
    password: str = Column(String, nullable=False)
    is_verify: str = Column(Boolean, default=False)
    created_at: datetime = Column(TIMESTAMP, default=datetime.now)