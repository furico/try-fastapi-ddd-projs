from typing import assert_never

from app.api.schemas.user import UserResponse
from app.domain.user import ActiveUser, BannedUser, User


def to_user_response(user: User) -> UserResponse:
    match user:
        case ActiveUser():
            status = "active"
        case BannedUser():
            status = "banned"
        case _:
            assert_never(user)

    return UserResponse(
        user_id=user.user_id,
        email=user.email,
        status=status,
    )
