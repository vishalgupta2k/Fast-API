from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import BookCreateModel, BookUpdate
from sqlmodel import select,desc
from .models import Book
from datetime import datetime
class BookService:

    # get_all_books metho working
    async def get_all_books(self,session:AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.execute(statement)
        if result is None:
            return None
        return result.scalars().all()

    #get_book method == working
    async def get_book(self,book_uid : str ,session:AsyncSession):
        statement = select(Book).where(Book.uid == book_uid) # select * from books where uid = book_uid
        result = await session.execute(statement) 
        book = result.scalar_one_or_none()  # get the book
        return book
    # craete book method == working
    async def create_book(self,book_data:BookCreateModel,session:AsyncSession):
        book_data_dict = book_data.model_dump()
        new_book = Book(**book_data_dict)
        session.add(new_book)
        await session.commit()
        return new_book
        
    # update_book method == working
    async def update_book(self,book_uid:str,update_data: BookUpdate,session:AsyncSession):
        book_to_update = await self.get_book(book_uid,session)
        if book_to_update is None:
            return None
        for key,value in update_data.items(): # update_data is a dictionary
            setattr(book_to_update,key,value)
        book_to_update.updated_at = datetime.utcnow() # update the updated_at field
        await session.commit() # commit the changes
        return book_to_update # return the updated book

    # delete_book method == working
    async def delete_book(self,book_uid:str,session:AsyncSession):
        book_to_delete = await self.get_book(book_uid,session)
        if book_to_delete is None:
            return None
        await session.delete(book_to_delete)
        await session.commit()
        return book_to_delete

