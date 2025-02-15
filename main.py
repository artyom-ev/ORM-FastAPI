from fastapi import Depends, FastAPI
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel, ConfigDict
from database import Base, BookModel, engine, get_session

app = FastAPI()

SessionDep = Annotated[AsyncSession, Depends(get_session)]

class BookSchema(BaseModel):
    title: str
    author: str

class BookGetSchema(BaseModel):
    id: int
    title: str
    author: str

    # Enable ORM mode for compatibility with SQLAlchemy models
    model_config = ConfigDict(from_attributes=True)

@app.post("/setup")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

@app.post("/books")
async def add_book(book: BookSchema, session: SessionDep) -> BookSchema:
    new_book = BookModel(
        title=book.title,
        author=book.author,
    )
    session.add(new_book)
    await session.commit()
    return book

@app.get("/books")
async def get_books(session: SessionDep) -> list[BookGetSchema]:
    query = select(BookModel)
    result = await session.execute(query)
    books = result.scalars().all()
    return [BookGetSchema.model_validate(book) for book in books]