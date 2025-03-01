from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import BookModel
from schemas import BookSchema, BookGetSchema
from database import engine, Base

async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return {"success": True}

async def add_book(book: BookSchema, session: AsyncSession) -> BookGetSchema:
    new_book = BookModel(title=book.title, author=book.author)
    session.add(new_book)
    await session.commit()
    await session.refresh(new_book)
    return BookGetSchema.model_validate(new_book)

async def get_books(session: AsyncSession) -> list[BookGetSchema]:
    query = select(BookModel)
    result = await session.execute(query)
    books = result.scalars().all()
    return [BookGetSchema.model_validate(book) for book in books]