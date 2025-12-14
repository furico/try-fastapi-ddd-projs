from typing import assert_never

from fastapi import APIRouter, Depends, HTTPException
from typing_extensions import assert_never

from app.api.deps import get_user_repository
from app.domain.user import ActiveUser, BannedUser
from app.infra.memory_user_repository import InMemoryUserRepository
from app.usecase.user import ban_user, get_user, register_user

router = APIRouter()


@router.post("/users")
def create_user(
    user_id: int,
    email: str,
    repo: InMemoryUserRepository = Depends(get_user_repository),
):
    user = register_user(user_id, email, repo)
    return {
        "user_id": user.user_id,
        "email": user.email,
        "status": "active",
    }


@router.get("/users/{user_id}")
def read_user(
    user_id: int,
    repo: InMemoryUserRepository = Depends(get_user_repository),
):
    user = get_user(user_id, repo)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    match user:
        case ActiveUser():
            status = "active"
        case BannedUser():
            status = "banned"
        case _:
            assert_never(user)

    return {
        "user_id": user.user_id,
        "email": user.email,
        "status": status,
    }


@router.post("/users/{user_id}/ban")
def ban_user_api(
    user_id: int,
    repo: InMemoryUserRepository = Depends(get_user_repository),
):
    banned = ban_user(user_id, repo)

    if banned is None:
        raise HTTPException(status_code=400, detail="Cannot ban user")

    return {
        "user_id": banned.user_id,
        "email": banned.email,
        "status": "banned",
    }
