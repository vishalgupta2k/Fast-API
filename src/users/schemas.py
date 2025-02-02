from pydantic import BaseModel,EmailStr
import uuid
from datetime import datetime

class User(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime

class UserCreateModel(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserLoginResponse(BaseModel):
    email: str
    token: str
    token_type: str
    username: str
    uid: uuid.UUID

class UserResponse(BaseModel):
    username: str
    email: EmailStr
    uid: uuid.UUID
    created_at: datetime
    updated_at: datetime

