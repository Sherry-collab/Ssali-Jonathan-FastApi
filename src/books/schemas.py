from pydantic import BaseModel
from datetime import datetime
from src.reviews.schemas import ReviewModel
from typing import List
import uuid

class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: datetime | None = None 
    created_at: datetime
    updated_at: datetime
    
class BookDetailModel(Book):
    reviews: List[ReviewModel]
    
class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: datetime
class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str