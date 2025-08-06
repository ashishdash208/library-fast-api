from fastapi import APIRouter, HTTPException, Query
from typing import List
from models.book_model import Book, BookCreate
import services.book_service as service

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=Book, status_code=201)
def create_book(book_data: BookCreate):
    return service.add_book(book_data)
