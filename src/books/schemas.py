from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    
class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str