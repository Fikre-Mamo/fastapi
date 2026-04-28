from fastapi import FastAPI, Body, Request
from fastapi.responses import HTMLResponse
import pydantic
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
    
books = [
    BOOK(1, "Mike and sytems", "Miko", "the best book to learn systems", 5),
    BOOK(2, "The live of API", "Fikre", "What you need to master API", 4.5),
    BOOK(3, "Fast with FastAPI", "Lio", "Code faster code smarter", 4.2),
    BOOK(4, "Nteworking and HTTP", "Jack Ma", "How to manage HTTP", 3.4),
    BOOK(5, "Python and use", "Fikre", "The way to master python", 4.2),
    BOOK(6, "Live death and robote", "Lio", "Learn how to countrol Hardware", 5)
]

@app.get("/books")
def list_books():
    return books