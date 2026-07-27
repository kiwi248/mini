# product_router.py
from fastapi import APIRouter, status

from app.schemes.product_scheme import PostCreate, PostGet, PostUpdate
from app.services.product_service import (
    post_create,
    post_delete,
    post_get,
    post_get_all,
    post_update,
)


product_router = APIRouter(prefix="/posts", tags=["posts"])


# 1. 게시글 등록
@product_router.post("", response_model=PostGet, status_code=status.HTTP_201_CREATED)
def create(post: PostCreate) -> PostGet:
    return post_create(post)


# 2. 게시글 전체 조회
@product_router.get("", response_model=list[PostGet])
def get_all() -> list[PostGet]:
    return post_get_all()


# 3. 게시글 단건 조회
@product_router.get("/{post_id}", response_model=PostGet)
def get(post_id: int) -> PostGet:
    return post_get(post_id)


# 4. 게시글 수정
@product_router.put("/{post_id}", response_model=PostGet)
def put(post_id: int, post: PostUpdate) -> PostGet:
    return post_update(post_id, post)


# 5. 게시글 삭제
@product_router.delete("/{post_id}", response_model=PostGet)
def delete(post_id: int) -> PostGet:
    return post_delete(post_id)
