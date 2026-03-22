from fastapi import APIRouter, HTTPException
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.schemas import UserCreate, UserResponse

router = APIRouter()

service = UserService(repo=UserRepository())

@router.get("/", response_model=list[UserResponse])
def list_users():
    users = service.repo.list_users()
    return [UserResponse(**u.__dict__) for u in users]

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(payload: UserCreate):
    created = service.create_user(payload)
    if not created:
        raise HTTPException(status_code=500, detail="Could not create user")
    return UserResponse(**created.__dict__)