from fastapi import HTTPException, status

from app.schemes.user_scheme import UserCreate, UserResponse, UserUpdate


# 미니 프로젝트 요구사항에 맞춘 메모리 저장소입니다.
fake_db: list[dict[str, object]] = []
_next_user_id = 1


def _to_response(user: dict[str, object]) -> UserResponse:
    return UserResponse(
        user_id=int(user["user_id"]),
        username=str(user["username"]),
        email=str(user["email"]),
        bio=user.get("bio"),
    )


def _find_user(user_id: int) -> dict[str, object]:
    for user in fake_db:
        if user["user_id"] == user_id:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="사용자를 찾을 수 없습니다.",
    )


def create_user(user: UserCreate) -> UserResponse:
    global _next_user_id

    saved_user = {"user_id": _next_user_id, **user.model_dump()}
    fake_db.append(saved_user)
    _next_user_id += 1
    return _to_response(saved_user)


def get_users() -> list[UserResponse]:
    return [_to_response(user) for user in fake_db]


def get_user(user_id: int) -> UserResponse:
    return _to_response(_find_user(user_id))


def update_user(user_id: int, user: UserUpdate) -> UserResponse:
    saved_user = _find_user(user_id)
    saved_user.update(user.model_dump())
    return _to_response(saved_user)


def delete_user(user_id: int) -> dict[str, int | str]:
    saved_user = _find_user(user_id)
    fake_db.remove(saved_user)
    return {"message": "삭제하였습니다.", "id": user_id}


def reset_users() -> None:
    """테스트마다 메모리 저장소와 ID를 초기화합니다."""
    global _next_user_id
    fake_db.clear()
    _next_user_id = 1
