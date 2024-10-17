from . import app
from db import Config,Book
from sqlalchemy import select
from ..schemas import CreateBook
from fastapi import status


Session=Config.SESSION


@app.get("/books")
def all_books():
    with Session() as session:
        books=session.scalars(select(Book)).all()
        return books

@app.post("/books",status_code=status.HTTP_201_CREATED)
def create_book(data:CreateBook):
    with Session.begin() as session:
        book = Book(**data.model_dump())
        session.add(book)
        return "Successfully created"
    

@app.get("/books/{id}")
def one_book(id:int):
    with Session() as session:
        book = session.scalar(select(Book).where(Book.id==id))
        return book

