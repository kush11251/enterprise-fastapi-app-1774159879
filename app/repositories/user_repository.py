from app.models import User
from typing import List, Optional

class UserRepository:
    def __init__(self):
        self._users = [User(id=1, username="alpha", email="alpha@example.com")]

    def list_users(self) -> List[User]:
        return list(self._users)

    def find_by_id(self, user_id: int) -> Optional[User]:
        return next((u for u in self._users if u.id == user_id), None)

    def create_user(self, username: str, email: str) -> User:
        new_id = max([u.id for u in self._users], default=0) + 1
        user = User(id=new_id, username=username, email=email)
        self._users.append(user)
        return user