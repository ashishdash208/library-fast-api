from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: int
    title: str
    author: str
    published_year: int
    available: bool = True

class BookCreate(BaseModel):
    title: str
    author: str
    published_year: int
