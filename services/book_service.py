from typing import List, Optional
from models.book_model import Book, BookCreate
import repositories.book_repository as repo

def add_book(book_data: BookCreate) -> Book:
    return repo.create_book(book_data)
