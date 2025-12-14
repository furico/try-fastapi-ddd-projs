from typing import Dict

from app.domain.user import User


class InMemoryUserRepository:
    """
    InMemoryUserRepository の Docstring
    """

    def __init__(self) -> None:
        self._users: Dict[int, User] = {}

    def get(self, user_id: int) -> User | None:
        return self._users.get(user_id)

    def save(self, user: User) -> None:
        self._users[user.user_id] = user
