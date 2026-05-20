from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'One', 'category': 'science'},
    {'title': 'Title two', 'author': 'One', 'category': 'science'},
    {'title': 'Title three', 'author': 'One', 'category': 'history'},
    {'title': 'Title four', 'author': 'four', 'category': 'math'},
    {'title': 'Title five', 'author': 'five', 'category': 'math'},
    {'title': 'Title six', 'author': 'six', 'category': 'math'}
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

    return {"message": "Book not found"}

@app.get("/books/")
async def read_category_by_query(category : str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}")
async def read_author_category_by_query(book_author : str , category : str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
                  books_to_return.append(book)
    return books_to_return

