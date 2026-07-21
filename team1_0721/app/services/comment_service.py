"""port 프로젝트의 임시 메모리 기반 댓글 CRUD 로직입니다."""

from datetime import datetime, timezone

from fastapi import HTTPException, status

from app.schemes.comment_scheme import CommentCreate, CommentGet, CommentUpdate


# Supabase를 사용하지 않는 학습용 임시 데이터입니다.
# Render 서버가 재시작되면 아래 초기 상태로 돌아갑니다.
fake_db: list[CommentGet] = [
    CommentGet(
        comment_id=1,
        post_id=1,
        user_id=1,
        content="첫 번째 게시글의 댓글입니다.",
        created_at="2026-07-21T09:00:00+09:00",
    ),
    CommentGet(
        comment_id=2,
        post_id=1,
        user_id=2,
        content="좋은 글 감사합니다.",
        created_at="2026-07-21T09:05:00+09:00",
    ),
    CommentGet(
        comment_id=3,
        post_id=2,
        user_id=1,
        content="두 번째 게시글의 댓글입니다.",
        created_at="2026-07-21T09:10:00+09:00",
    ),
]
_next_comment_id = 4


def _find_comment_index(comment_id: int) -> int:
    """댓글 번호에 해당하는 목록 위치를 찾습니다."""
    for index, comment in enumerate(fake_db):
        if comment.comment_id == comment_id:
            return index

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Comment not found",
    )


def comment_create(comment: CommentCreate) -> CommentGet:
    """새 댓글을 임시 저장소에 추가합니다."""
    global _next_comment_id

    created_comment = CommentGet(
        comment_id=_next_comment_id,
        post_id=comment.post_id,
        user_id=comment.user_id,
        content=comment.content.strip(),
        created_at=datetime.now(timezone.utc).isoformat(),
    )
    fake_db.append(created_comment)
    _next_comment_id += 1
    return created_comment


def comment_get_all() -> list[CommentGet]:
    """저장된 모든 댓글을 조회합니다."""
    return list(fake_db)


def comment_get(comment_id: int) -> CommentGet:
    """댓글 번호로 댓글 한 개를 조회합니다."""
    return fake_db[_find_comment_index(comment_id)]


def comment_get_by_post(post_id: int) -> list[CommentGet]:
    """특정 게시글에 작성된 댓글을 조회합니다."""
    return [comment for comment in fake_db if comment.post_id == post_id]


def comment_update(comment: CommentUpdate) -> CommentGet:
    """댓글 내용을 수정합니다."""
    index = _find_comment_index(comment.comment_id)
    saved_comment = fake_db[index]
    updated_comment = CommentGet(
        comment_id=saved_comment.comment_id,
        post_id=saved_comment.post_id,
        user_id=saved_comment.user_id,
        content=comment.content.strip(),
        created_at=saved_comment.created_at,
    )
    fake_db[index] = updated_comment
    return updated_comment


def comment_delete(comment_id: int) -> CommentGet:
    """댓글을 삭제하고 삭제한 내용을 반환합니다."""
    return fake_db.pop(_find_comment_index(comment_id))
