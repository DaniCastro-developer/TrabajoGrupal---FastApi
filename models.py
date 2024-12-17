from pydantic import BaseModel

class BookModel(BaseModel):
    id: str
    name: str
    publisher: str
    year: str
    edition: int
    authors: str