from typing import List
from fastapi import APIRouter

from app.dto.user import UserRequest, UserResponse
from app.repository.memory import MemoryRepository
from app.use_case.user import UserAddUseCase, UserListUseCase

router = APIRouter()

repo = MemoryRepository()


@router.get("/users/")
async def get_users() -> List[UserResponse]:
    return [UserResponse.from_orm(e) for e in UserListUseCase(repo).execute()]


@router.post("/users/")
async def create_user(user: UserRequest) -> UserResponse:
    entity = UserAddUseCase(repo).execute(user)

    return UserResponse.from_orm(entity)
