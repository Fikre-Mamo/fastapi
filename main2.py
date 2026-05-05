from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional
import uvicorn


app = FastAPI()

class BOOK:
    id = int
    book_name = str
    author_name = str
    description = str
    rating = float

    def __init__(self, id, book_name, author_name, description, rating):
        self.id = id
        self.book_name = book_name
        self.author_name = author_name
        self.description = description
        self.rating = rating
    
class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not neded on create', default=None)
    book_name: str = Field(min_length=3, max_length=100)
    author_name: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=10, max_length=200)
    rating: float = Field(ge=0, le=6)

model_config = {
        "json_schema_extra":{
            "example":{
                "title": "A new book",
                "author": "Fikre Miko",
                "description": "The new era of coding",
                "rating": 5
                }
            }
        }


books = [
    BOOK(1, "Mike and sytems", "Miko", "the best book to learn systems", 5),
    BOOK(2, "The live of API", "Fikre", "What you need to master API", 4.5),
    BOOK(3, "Fast with FastAPI", "Lio", "Code faster code smarter", 4.2),
    BOOK(4, "Nteworking and HTTP", "Jack Ma", "How to manage HTTP", 3.4),
    BOOK(5, "Python and use", "Fikre", "The way to master python", 4.2),
    BOOK(6, "Live death and robote", "Lio", "Learn how to countrol Hardware", 5)
]
@app.get("/")
def welcome():
    return "message: Welcome to the book store"

@app.get("/books")
def list_books():
    return books

@app.post("/book")
def create_book(book: BookRequest):
    if len(books) > 0:
        book.id = books[-1].id + 1
    else:
        book.id = 1
    return book

@app.post("/create_new_book")
def create_new_book(book: BookRequest):
    new_book = BOOK(**book.model_dump())
    books.append(new_book)
    return new_booki



if __name__ == "__main__":
    uvicorn.run("main2:app", host="127.0.0.1", port=8000, reload=True)
