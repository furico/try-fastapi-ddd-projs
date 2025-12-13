from typing import Protocol
from app.domain.user import User


class UserRepository(Protocol):
    def get(self, user_id: int) -> User | None:
        """ユーザーを取得する。存在しない場合は None を返す。"""
        ...

    def save(self, user: User) -> None:
        """ユーザーを保存する。"""
        ...
