# product_scheme.py
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class PostCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200, examples=["첫 번째 글"])
    content: str = Field(min_length=1, examples=["게시글 내용입니다."])
    author: str = Field(min_length=1, max_length=100, examples=["홍길동"])


class PostUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    content: str | None = Field(default=None, min_length=1)
    author: str | None = Field(default=None, min_length=1, max_length=100)


class PostGet(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: int
    title: str
    content: str
    author: str
    created_at: datetime
    updated_at: datetime | None = None
