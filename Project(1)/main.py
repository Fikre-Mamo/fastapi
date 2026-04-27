from fastapi import Body, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
from fastapi.templating import Jinja2Templates
import uvicorn

# Create FastAPI instance
app = FastAPI()

# Create the books list
BOOKS = [
    {"id": 1, "title": "First Book", "author": "Author One", "category": "Bio"},
    {"id": 2, "title": "Second Book", "author": "Author Two", "category": "Art"},
    {"id": 3, "title": "Third Book", "author": "Author Three", "category": "Science"}
]

# Add a new books to the list
BOOKS.append({"id": 4, "title": "Fourth Book", "author": "Author Four", "category": "Bio"})
BOOKS.append({"id": 5, "title": "Fifth Book", "author": "Author Five", "category": "Art"})
BOOKS.append({"id": 6, "title": "Sixth Book", "author": "Author Two", "category": "Science"})

# create the read_root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}

# create the read_books endpoint
@app.get("/books")
def read_books():
    return BOOKS

# fillter by author endpoint
@app.get("/books/author/{author_name}")
def filter_by_author(author_name: str):
    book_to_return = []
    for i in BOOKS:
        if i.get("author").casefold() == author_name.casefold():
            book_to_return.append(i)
    return book_to_return


# create the read_category_by_query endpoint
@app.get("/books/")
def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# create the read_books_by_author endpoint
@app.get("/books/{book_author}")
def read_books_by_author(book_author: str, category: Optional[str] = None):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() or \
        (book.get("category").casefold() == category.casefold()):
            books_to_return.append(book)
    return books_to_return

# create the read_only_books endpoint
@app.get("/book/{read_book}")
def read_only_books(read_book: str):
    for book in BOOKS:
        if book.get("title").casefold() == read_book.casefold():
            return book

# create the create_book endpoint
@app.post("/books/new_book")
def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return {"message": "Book added successfully!"}

# create the update_books endpoint
@app.put("/books/update_book")
def update_books(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("titles") == updated_book.get("titles"):
            BOOKS[i] = updated_book
            return {"message": "Book updated successfully!"}

# create the delete_book endpoint
@app.delete("/books/delete_book/{book_title}")
def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
    return {"message": "Book deleted successfully!"}




# Mount static files
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
