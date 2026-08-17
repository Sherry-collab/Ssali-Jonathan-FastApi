from pydantic import BaseModel
from datetime import datetime
import uuid

class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: str
    created_at: datetime
    upadte_at: datetime
    
class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str