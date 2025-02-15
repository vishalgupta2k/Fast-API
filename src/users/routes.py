from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from typing import List
from src.users.schemas import User, UserCreateModel, UserResponse
from src.db.main import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
from src.users.service import UserService
router = APIRouter()
user_service = UserService()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def add_user(user_data: UserCreateModel, session: AsyncSession = Depends(get_session)) -> dict:
    new_user = await user_service.create_user(user_data, session)
    new_user_dict = new_user.dict()
    return new_user
