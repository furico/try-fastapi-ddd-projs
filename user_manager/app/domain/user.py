from dataclasses import dataclass
from typing import Union


# ----------------------------------------
# ドメインモデル
#
# User は「状態」を持ち、状態ごとに可能な操作が異なる。
# 状態はフラグではなく型で表現する。
# ----------------------------------------
@dataclass(frozen=True)
class ActiveUser:
    user_id: int
    email: str


@dataclass(frozen=True)
class BannedUser:
    user_id: int
    email: str


User = Union[ActiveUser, BannedUser]


# ----------------------------------------
# ドメインロジック
#
# 状態遷移は関数として定義し、不正な遷移は型で防ぐ。
# ----------------------------------------
def ban(user: ActiveUser) -> BannedUser:
    return BannedUser(
        user_id=user.user_id,
        email=user.email,
    )
