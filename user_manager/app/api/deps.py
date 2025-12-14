from app.infra.memory_user_repository import InMemoryUserRepository

_repo = InMemoryUserRepository()


def get_user_repository() -> InMemoryUserRepository:
    # 本来は request ごと / session ごとに切り替える
    return _repo
