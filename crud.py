from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

books = [
    {
    "id" : 1,
    "title" : "The Alchemist",
    "author" : "Paulo Coelho",
    "publish_date" : "1988-01-01"
    },

    {
    "id" : 2,
    "title" : "The God of Small Things",
    "author" : "Arundhathi Roy",
    "publish_date" : "1997-04-04"
    },

    {
    "id" : 3,
    "title" : "The White Tiger",
    "author" : "Aravind Adiga",
    "publish_date" : "2008-01-01"
    },

    {
    "id" : 4,
    "title" : "The Palace of Illusions",
    "author" : "Chitra Benerjee Divakaruni",
    "publish_date" : "2008-02-12"
    },
]

app = FastAPI()

@app.get("/book")
def get_book():
    return books

@app.get("/book/{book_id}")
def get_book(book_id: int ):
    for book in books:
        if book['id'] == book_id:
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , deatil= "Book not Found")

class Book(BaseModel):
    id : int
    title : str
    author : str
    Publish_date : str
    
@app.post("/post")
def create_book(book: Book):
    new_book = book.model_dump()  # model_dump() --> convert a Pydantic model instance into a Python dictionary
    books.append(new_book)
    return new_book
    
class BookUpdate(BaseModel):
    title : str
    author : str
    Publish_date : str

@app.put("/book/{book_id}")
def update_book(book_id: int, book_update : BookUpdate):
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update.title
            book['author'] =book_update.author
            book['publish_date'] = book_update.Publish_date
            return book
        
@app.delete("/book/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {"Message": "our book deleted"}

