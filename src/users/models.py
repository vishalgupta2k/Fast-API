from sqlmodel import SQLModel, Field, Column
from datetime import datetime, date
import uuid
import sqlalchemy.dialects.postgresql as postgresql

class User (SQLModel, table=True):
    __tablename__ = "users"
    uid :uuid.UUID = Field(
        sa_column = Column(
            postgresql.UUID,
            primary_key = True,
            nullable = False,
            default = uuid.uuid4
        )
    )
    username: str
    email: str = Field(
        sa_column = Column(
            postgresql.VARCHAR(255),
            nullable = False,
            unique = True
        )
    )
    password: str= Field(exclude = True)
    isVerified : bool = Field(default = False)
    created_at: datetime= Field(
        sa_column = Column(
            postgresql.TIMESTAMP,
            nullable = False,
            default = datetime.utcnow()
        )
    )
    updated_at: datetime = Field(
        sa_column = Column(
            postgresql.TIMESTAMP,
            nullable = False,
            default = datetime.utcnow()
        )
    ) 


    def __repr__(self):
        return f"User {self.username} with email {self.email}"