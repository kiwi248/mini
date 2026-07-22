from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    username: str = Field(min_length=1)
    email: str = Field(min_length=1)
    password: str = Field(min_length=1)
    bio: str | None = None


class UserUpdate(BaseModel):
    username: str = Field(min_length=1)
    email: str = Field(min_length=1)
    password: str = Field(min_length=1)
    bio: str | None = None


class UserResponse(BaseModel):
    user_id: int
    username: str
    email: str
    bio: str | None = None


class DeleteResponse(BaseModel):
    message: str
    id: int
