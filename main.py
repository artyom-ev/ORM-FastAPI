from fastapi import Depends, FastAPI
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import select
from pydantic import BaseModel, ConfigDict
import os
from dotenv import load_dotenv

load_dotenv()

# Database setup
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

app = FastAPI()

database_url = f"postgresql+asyncpg://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_async_engine(database_url, echo=True)
new_async_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_async_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]

class Base(DeclarativeBase):
    pass

class BookModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]

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