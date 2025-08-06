from typing import List, Optional
from models.book_model import Book, BookCreate
import repositories.book_repository as repo

def add_book(book_data: BookCreate) -> Book:
    return repo.create_book(book_data)
def remove_book(book_id: int) -> bool:
    return repo.delete_book(book_id)

def set_availability(book_id: int, available: bool) -> Optional[Book]:
    return repo.update_availability(book_id, available)