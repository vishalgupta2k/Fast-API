from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from typing import List
from src.books.book_data import books
from src.books.schemas import Book, BookUpdate

router = APIRouter()

# @router.get("/")
# async def root_check():
#     return {"message": "your Server is running"}

@router.get("/", response_model=dict)
async def get_books():
    return {"data": books, "status": 200, "message": "Books retrieved successfully"}

@router.get("/{book_id}", response_model=dict)
async def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return {"data": book, "status": 200, "message": "Book retrieved successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_book( book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return {"message": "Book added successfully", "status": 201, "data": new_book}

@router.put("/{book_id}")
async def update_book(book_id: int, book_data: BookUpdate, status_code=status.HTTP_204_NO_CONTENT):
    new_data = book_data.model_dump()
    for book in books:
        if book["id"] == book_id:
            book.update(new_data)
            return {"message": "Book updated successfully", "status":status_code ,"data": new_data}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@router.delete("/{book_id}")
async def delete_book(book_id: int, status_code=status.HTTP_204_NO_CONTENT):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted", "status": 204, "data": book}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")