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

def delete_book(book_id: int) -> bool:
    for i, book in enumerate(book_db):
        if book.id == book_id:
            del book_db[i]
            return True
    return False

def update_availability(book_id: int, available: bool) -> Optional[Book]:
    book = get_book_by_id(book_id)
    if book:
        book.available = available
        return book
    return None
