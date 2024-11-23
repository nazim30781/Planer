from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: str
    password: str = Field(min_length=8)


class UserCreateModel(UserBase):
    pass