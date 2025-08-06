from fastapi import APIRouter, HTTPException, Query
from typing import List
from models.book_model import Book, BookCreate
import services.book_service as service

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=Book, status_code=201)
def create_book(book_data: BookCreate):
    return service.add_book(book_data)
@router.delete("/{book_id}")
def delete_book(book_id: int):
    success = service.remove_book(book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"detail": "Book deleted"}

@router.patch("/{book_id}/availability", response_model=Book)
def update_availability(book_id: int, available: bool = Query(...)):
    book = service.set_availability(book_id, available)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book