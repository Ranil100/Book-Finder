from dataclasses import field
from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

class Book():
   def __init__(self ,id ,title, author, description,rating):
      self.id = id
      self.title = title
      self.author = author
      self.description = description
      self.rating = rating


class BookRequest(BaseModel):
        id: int
        title: str = Field(min_length = 3)
        author: str = Field(min_length = 3)
        description: str = Field(min_length = 3,max_length= 100)
        rating: int = Field(gt= 0, lt= 6)

BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1)
]

@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create")
async def create_book(book_request: BookRequest):
     new_book = Book(**book_request.dict())
     find_book_id(new_book)
     BOOKS.append(new_book)

def find_book_id(book : Book):
    if len(BOOKS) > 0:
        Book.id = BOOKS[-1].id + 1
    else:
        Book.id = 1

    return book

