# product_service.py
import os
from typing import Any, Callable

from fastapi import HTTPException, status

from app.core.supabase_client import get_supabase
from app.schemes.product_scheme import PostCreate, PostGet, PostUpdate


POSTS_TABLE = os.getenv("SUPABASE_POSTS_TABLE", "posts")


def _execute(query: Callable[[], Any], message: str) -> Any:
    try:
        return query().execute()
    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=message,
        ) from error


def _first_or_404(data: list[dict[str, Any]] | None) -> PostGet:
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="게시글을 찾을 수 없습니다.",
        )
    return PostGet.model_validate(data[0])


# 1. 게시글 등록
def post_create(post: PostCreate) -> PostGet:
    response = _execute(
        lambda: get_supabase()
        .table(POSTS_TABLE)
        .insert(post.model_dump()),
        "게시글 등록 중 오류가 발생했습니다.",
    )
    return _first_or_404(response.data)


# 2. 게시글 전체 조회
def post_get_all() -> list[PostGet]:
    response = _execute(
        lambda: get_supabase()
        .table(POSTS_TABLE)
        .select("*")
        .order("created_at", desc=True),
        "게시글 목록 조회 중 오류가 발생했습니다.",
    )
    return [PostGet.model_validate(post) for post in (response.data or [])]


# 3. 게시글 단건 조회
def post_get(post_id: int) -> PostGet:
    response = _execute(
        lambda: get_supabase()
        .table(POSTS_TABLE)
        .select("*")
        .eq("id", post_id)
        .limit(1),
        "게시글 조회 중 오류가 발생했습니다.",
    )
    return _first_or_404(response.data)


# 4. 게시글 수정
def post_update(post_id: int, post: PostUpdate) -> PostGet:
    update_data = post.model_dump(exclude_none=True)
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="수정할 내용을 하나 이상 입력해 주세요.",
        )

    response = _execute(
        lambda: get_supabase()
        .table(POSTS_TABLE)
        .update(update_data)
        .eq("id", post_id),
        "게시글 수정 중 오류가 발생했습니다.",
    )
    return _first_or_404(response.data)


# 5. 게시글 삭제
def post_delete(post_id: int) -> PostGet:
    response = _execute(
        lambda: get_supabase()
        .table(POSTS_TABLE)
        .delete()
        .eq("id", post_id),
        "게시글 삭제 중 오류가 발생했습니다.",
    )
    return _first_or_404(response.data)
