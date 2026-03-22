from app.repositories.user_repository import UserRepository
from app.schemas import UserCreate

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def get_user(self, user_id: int):
        return self.repo.find_by_id(user_id)

    def create_user(self, created: UserCreate):
        return self.repo.create_user(created.username, created.email)