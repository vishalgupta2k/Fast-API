from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from typing import List
# from src.books.book_data import books
from src.books.schemas import Book, BookUpdate,BookCreateModel
from src.db.main import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
from src.books.service import BookService
router = APIRouter()
book_service = BookService()

@router.get("/", response_model=List[Book])
async def get_books(session: AsyncSession = Depends(get_session),status_code=status.HTTP_200_OK):
    books = await book_service.get_all_books(session)
    print(books)
    if books is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No books found")

    return books


@router.get("/{book_uid}", response_model=dict)
async def get_book(book_uid: str,session: AsyncSession = Depends(get_session) ,status_code=status.HTTP_200_OK):
    book =  await book_service.get_book(book_uid, session)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return {"data": book, "status": status_code, "message": "Book retrieved successfully"}

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=dict)
async def add_book( book_data: BookCreateModel,session: AsyncSession = Depends(get_session)) -> dict:
    new_book = await book_service.create_book(book_data,session)
    return {"message": "Book added successfully", "status": 201, "data": new_book}


@router.put("/{book_uid}")
async def update_book(book_uid: str, book_data: BookUpdate, session: AsyncSession = Depends(get_session), status_code=status.HTTP_204_NO_CONTENT):
    new_data = book_data.model_dump()
    updated_book = await book_service.update_book(book_uid, new_data, session)
    if updated_book is not None:
        return {"message": "Book updated successfully", "status":status_code ,"data": updated_book}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@router.delete("/{book_uid}")
async def delete_book(book_uid: str, session: AsyncSession = Depends(get_session),status_code=status.HTTP_204_NO_CONTENT):
    book = await book_service.delete_book(book_uid, session)
    if book is not None:
        return {"message": "Book deleted", "status": 204, "data": book}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")