from sqlmodel import SQLModel, Field, Column
from datetime import datetime, date
import uuid
import sqlalchemy.dialects.postgresql as postgresql

class Book(SQLModel, table=True):
    __tablename__ = "books"
    uid :uuid.UUID = Field(
        sa_column = Column(
            postgresql.UUID,
            primary_key = True,
            nullable = False,
            default = uuid.uuid4
        )
    )
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
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
        return f"Book {self.title} by {self.author}"
