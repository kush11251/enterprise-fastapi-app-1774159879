from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.schemas import UserCreate

def test_create_and_fetch_user():
    repo = UserRepository()
    service = UserService(repo=repo)

    created = service.create_user(UserCreate(username="bravo", email="bravo@example.com"))
    assert created.id == 2

    fetched = service.get_user(2)
    assert fetched is not None
    assert fetched.username == "bravo"