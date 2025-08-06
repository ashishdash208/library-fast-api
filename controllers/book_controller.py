from fastapi import APIRouter, HTTPException, Query
from typing import List
from models.book_model import Book, BookCreate
import services.book_service as service

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=Book, status_code=201)
def create_book(book_data: BookCreate):
    return service.add_book(book_data)

@router.get("/", response_model=List[Book])
def get_books():
    return service.list_books()

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = service.find_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book