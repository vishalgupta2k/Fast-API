from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.exceptions import HTTPException
from .schemas import UserCreateModel,UserLogin,LoginUserResponse,LoginResponse
from sqlmodel import select,desc
from .models import User
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .utils import create_access_token
from src.config import Config
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class UserService:
    async def create_user(self,user_data:UserCreateModel,session:AsyncSession):
        user_data_dict = user_data.model_dump()
        hashed_password = pwd_context.hash(user_data_dict['password'])
        user_data_dict['password'] = hashed_password
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
    async def login_user(self, user_data: UserLogin, session: AsyncSession):
        result = await session.execute(select(User).where(User.email == user_data.email))
        user = result.scalars().first()
        
        if not user:
            raise HTTPException(status_code=400, detail="User not found")
        
        if not pwd_context.verify(user_data.password, user.password):
            raise HTTPException(status_code=400, detail="Invalid password or email")
        
        access_token_expires = timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires,
        )
        
        user_response = LoginUserResponse(
            username=user.username,
            email=user.email,
            uid=user.uid,
        )
        
        return LoginResponse(token=access_token, token_type="bearer", user=user_response)