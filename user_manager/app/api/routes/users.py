from fastapi import APIRouter, Depends, HTTPException

from app.api.deps import get_user_repository
from app.api.presenters.user import to_user_response
from app.api.schemas.user import UserResponse
from app.infra.memory_user_repository import InMemoryUserRepository
from app.usecase.user import ban_user, get_user, register_user

router = APIRouter()


@router.post("/users", response_model=UserResponse)
def create_user(
    user_id: int,
    email: str,
    repo: InMemoryUserRepository = Depends(get_user_repository),
):
    user = register_user(user_id, email, repo)
    return to_user_response(user)


@router.get("/users/{user_id}", response_model=UserResponse)
def read_user(
    user_id: int,
    repo: InMemoryUserRepository = Depends(get_user_repository),
):
    user = get_user(user_id, repo)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return to_user_response(user)


@router.post("/users/{user_id}/ban", response_model=UserResponse)
def ban_user_api(
    user_id: int,
    repo: InMemoryUserRepository = Depends(get_user_repository),
):
    banned = ban_user(user_id, repo)

    if banned is None:
        raise HTTPException(status_code=400, detail="Cannot ban user")

    return to_user_response(banned)
