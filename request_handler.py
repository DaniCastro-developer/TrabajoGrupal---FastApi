from fastapi import FastAPI, HTTPException
import book_services
from models import BookModel

app = FastAPI()

#TODO: documentation - update 

@app.get("/book/all")
def get_all_books():
    result = book_services.get_book_all()
    return result

@app.get("/book/{book_id}")
def get_book_by_id(book_id: str):
    result = book_services.get_book_by_id(book_id)
    return result

@app.post("/book")
def add_new_book(book: BookModel):
    if not book_services.add_book(book):
        raise HTTPException(status_code=400, detail="Bad Request")
    
@app.delete("/book/{book_id}")
def delete_book(book_id: str):
    if not book_services.delete_book_by_id(book_id):
        raise HTTPException(status_code=400, detail="Bad Request")

#TODO: review this domain
#review books
@app.get("/book-reviews/{book_id}")
def get_book_by_id(book_id: str):
    result = book_services.get_book_review_by_id(book_id)
    return result