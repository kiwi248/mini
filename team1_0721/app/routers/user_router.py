from fastapi import APIRouter, status

from app.schemes.user_scheme import (
    DeleteResponse,
    UserCreate,
    UserResponse,
    UserUpdate,
)
from app.services.user_service import (
    create_user,
    delete_user,
    get_user,
    get_users,
    update_user,
)


user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create(user: UserCreate) -> UserResponse:
    return create_user(user)


@user_router.get("", response_model=list[UserResponse])
def get_all() -> list[UserResponse]:
    return get_users()


@user_router.get("/{user_id}", response_model=UserResponse)
def get_one(user_id: int) -> UserResponse:
    return get_user(user_id)


@user_router.put("/{user_id}", response_model=UserResponse)
def put(user_id: int, user: UserUpdate) -> UserResponse:
    return update_user(user_id, user)


@user_router.delete("/{user_id}", response_model=DeleteResponse)
def delete(user_id: int) -> dict[str, int | str]:
    return delete_user(user_id)
