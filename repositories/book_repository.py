from typing import List, Optional
from models.book_model import Book, BookCreate

# Mock DB
book_db: List[Book] = []
id_counter = 1

def create_book(book_data: BookCreate) -> Book:
    global id_counter
    new_book = Book(id=id_counter, **book_data.dict())
    book_db.append(new_book)
    id_counter += 1
    return new_book
