from typing import List, Optional
from models.book_model import Book, BookCreate
import repositories.book_repository as repo

def add_book(book_data: BookCreate) -> Book:
    return repo.create_book(book_data)

def list_books() -> List[Book]:
    return repo.get_all_books()

def find_book(book_id: int) -> Optional[Book]:
    return repo.get_book_by_id(book_id)
