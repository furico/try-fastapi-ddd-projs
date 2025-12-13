from typing import assert_never
from domain.user import User, ActiveUser, BannedUser, ban
from domain.repository import UserRepository


def get_user(
    user_id: int,
    repo: UserRepository,
) -> User | None:
    return repo.get(user_id)


def register_user(
    user_id: int,
    email: str,
    repo: UserRepository,
) -> ActiveUser:
    user = ActiveUser(user_id=user_id, email=email)
    repo.save(user)
    return user


def ban_user(
    user_id: int,
    repo: UserRepository,
) -> BannedUser | None:
    user = repo.get(user_id)

    if user is None:
        return None

    match user:
        case ActiveUser():
            banned = ban(user)
            repo.save(banned)
            return banned
        case BannedUser():
            return None
        case _:
            assert_never(user)
