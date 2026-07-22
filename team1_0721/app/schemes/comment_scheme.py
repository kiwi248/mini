"""port 프로젝트의 댓글 API 요청 및 응답 형식입니다."""

from pydantic import BaseModel, Field, PositiveInt, constr


CommentContent = constr(strip_whitespace=True, min_length=1)


class CommentCreate(BaseModel):
    """댓글 생성 요청입니다."""

    post_id: PositiveInt = Field(examples=[1])
    user_id: PositiveInt = Field(examples=[1])
    content: CommentContent = Field(examples=["좋은 글 감사합니다."])


class CommentUpdate(BaseModel):
    """댓글 수정 요청입니다."""

    comment_id: PositiveInt = Field(examples=[1])
    content: CommentContent = Field(examples=["수정한 댓글입니다."])


class CommentGet(BaseModel):
    """댓글 API 응답입니다."""

    comment_id: int
    post_id: int
    user_id: int
    content: str
    created_at: str
