from app.domain.user import ActiveUser, BannedUser
from app.infra.memory_user_repository import InMemoryUserRepository
from app.usecase.user import ban_user, get_user, register_user


def test_register_and_get_user():
    """登録 → 取得"""
    repo = InMemoryUserRepository()

    # ユーザー登録
    user = register_user(
        user_id=1,
        email="test@example.com",
        repo=repo,
    )

    fetched = get_user(1, repo)

    assert fetched == user
    assert isinstance(fetched, ActiveUser)


def test_ban_active_user():
    """BANできる"""
    repo = InMemoryUserRepository()

    register_user(1, "a@example.com", repo)

    banned = ban_user(1, repo)

    assert banned is not None
    assert isinstance(banned, BannedUser)

    stored = get_user(1, repo)
    assert isinstance(stored, BannedUser)


def test_ban_nonexistent_user():
    """存在しないユーザーはBANできない"""
    repo = InMemoryUserRepository()

    banned = ban_user(999, repo)

    assert banned is None


def test_ban_already_banned_user():
    """すでにBANされているユーザーは再度BANできない"""
    repo = InMemoryUserRepository()

    register_user(1, "a@example.com", repo)
    ban_user(1, repo)

    banned_again = ban_user(1, repo)

    assert banned_again is None
