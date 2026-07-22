"""port 프로젝트의 댓글 CRUD API 라우터입니다."""

from fastapi import APIRouter, status
from pydantic import PositiveInt

from app.schemes.comment_scheme import CommentCreate, CommentGet, CommentUpdate
from app.services.comment_service import (
    comment_create,
    comment_delete,
    comment_get,
    comment_get_all,
    comment_get_by_post,
    comment_update,
)


comment_router = APIRouter(tags=["comments"])


# 댓글 생성
@comment_router.post(
    "/comment/create",
    response_model=CommentGet,
    status_code=status.HTTP_201_CREATED,
)
def create(comment: CommentCreate) -> CommentGet:
    return comment_create(comment)


# 전체 댓글 조회: 동적 경로보다 먼저 등록해야 /getall이 올바르게 동작합니다.
@comment_router.get("/comment/getall", response_model=list[CommentGet])
def get_all() -> list[CommentGet]:
    return comment_get_all()


# 게시글별 댓글 조회
@comment_router.get(
    "/comment/post/{post_id}",
    response_model=list[CommentGet],
)
def get_by_post(post_id: PositiveInt) -> list[CommentGet]:
    return comment_get_by_post(post_id)


# 댓글 한 개 조회
@comment_router.get("/comment/get/{comment_id}", response_model=CommentGet)
def get(comment_id: PositiveInt) -> CommentGet:
    return comment_get(comment_id)


# 댓글 수정
@comment_router.put("/comment/put", response_model=CommentGet)
def put(comment: CommentUpdate) -> CommentGet:
    return comment_update(comment)


# 댓글 삭제
@comment_router.delete(
    "/comment/delete/{comment_id}",
    response_model=CommentGet,
)
def delete(comment_id: PositiveInt) -> CommentGet:
    return comment_delete(comment_id)
