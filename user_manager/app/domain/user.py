from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class ActiveUser:
    user_id: int
    email: str


@dataclass(frozen=True)
class BannedUser:
    user_id: int
    email: str


User = Union[ActiveUser, BannedUser]


def ban(user: ActiveUser) -> BannedUser:
    return BannedUser(
        user_id=user.user_id,
        email=user.email,
    )
