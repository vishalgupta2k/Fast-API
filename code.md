project/
├── app/
│ ├── **init**.py
│ ├── main.py
│ ├── api/
│ │ ├── **init**.py
│ │ ├── v1/
│ │ ├── **init**.py
│ │ ├── users.py
│ ├── core/
│ │ ├── **init**.py
│ │ ├── config.py
│ ├── db/
│ │ ├── **init**.py
│ │ ├── models.py
│ │ ├── session.py
│ ├── schemas/
│ │ ├── **init**.py
│ │ ├── user.py
│ ├── services/
│ │ ├── **init**.py
│ │ ├── user.py
│ ├── utils/
│ ├── **init**.py
│

# File: app/main.py

from fastapi import FastAPI
from app.api.v1.users import router as users_router

app = FastAPI()

# Include user routes in the application with versioning

app.include_router(users_router, prefix="/api/v1/users", tags=["Users"])

# File: app/api/v1/users.py

from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.services.user import create_user, get_user, update_user, delete_user

router = APIRouter()

# Endpoint to create a new user

@router.post("/", response_model=UserResponse)
def create(user: UserCreate): # Call the service layer to handle the creation logic
return create_user(user)

# Endpoint to retrieve a user by ID

@router.get("/{user_id}", response_model=UserResponse)
def read(user_id: int):
user = get_user(user_id)
if not user: # Raise an error if the user is not found
raise HTTPException(status_code=404, detail="User not found")
return user

# Endpoint to update an existing user

@router.put("/{user_id}", response_model=UserResponse)
def update(user_id: int, user: UserUpdate):
return update_user(user_id, user)

# Endpoint to delete a user by ID

@router.delete("/{user_id}")
def delete(user_id: int):
delete_user(user_id)
return {"message": "User deleted successfully"}

# File: app/schemas/user.py

from pydantic import BaseModel

# Base schema for shared user fields

class UserBase(BaseModel):
name: str
email: str

# Schema for creating a new user

class UserCreate(UserBase):
password: str

# Schema for updating an existing user

class UserUpdate(UserBase):
pass

# Schema for returning user details in responses

class UserResponse(UserBase):
id: int

    class Config:
        # Enable ORM mode for compatibility with SQLAlchemy models
        orm_mode = True

# File: app/db/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for all database models

Base = declarative_base()

# User model representing the users table in the database

class User(Base):
**tablename** = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

# File: app/db/session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URL for SQLite (can be replaced with another database)

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create a database engine

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Configure a session factory

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# File: app/services/user.py

from sqlalchemy.orm import Session
from app.db.models import User
from app.db.session import SessionLocal
from app.schemas.user import UserCreate, UserUpdate

# Dependency to provide a database session

def get_db():
db = SessionLocal()
try:
yield db
finally:
db.close()

# Service to create a new user in the database

def create_user(user: UserCreate):
db = next(get_db())
new_user = User(name=user.name, email=user.email, password=user.password)
db.add(new_user)
db.commit()
db.refresh(new_user) # Refresh to get the updated state from the database
return new_user

# Service to retrieve a user by ID

def get_user(user_id: int):
db = next(get_db())
return db.query(User).filter(User.id == user_id).first()

# Service to update an existing user

def update_user(user_id: int, user: UserUpdate):
db = next(get_db())
db_user = db.query(User).filter(User.id == user_id).first()
if not db_user:
raise HTTPException(status_code=404, detail="User not found") # Update only the fields provided in the request
for key, value in user.dict(exclude_unset=True).items():
setattr(db_user, key, value)
db.commit()
db.refresh(db_user)
return db_user

# Service to delete a user by ID

def delete_user(user_id: int):
db = next(get_db())
db_user = db.query(User).filter(User.id == user_id).first()
if not db_user:
raise HTTPException(status_code=404, detail="User not found")
db.delete(db_user)
db.commit()
