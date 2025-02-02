from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.exceptions import HTTPException
from .schemas import UserCreateModel
from sqlmodel import select,desc
from .models import User
from datetime import datetime

class UserService:
    async def create_user(self,user_data:UserCreateModel,session:AsyncSession):
        user_data_dict = user_data.model_dump()
        new_user = User(**user_data_dict)
        session.add(new_user)
        try :    
            await session.commit()
        except Exception as e:
            await session.rollback()
            print(e, "error")
            if "duplicate key value violates unique constraint" in str(e):
                raise HTTPException(status_code=400, detail="Email already exists")
            raise e
        session.refresh(new_user)
        return new_user