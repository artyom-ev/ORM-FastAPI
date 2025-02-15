from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models.book import BookModel

class BookRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_book(self, title: str, author: str) -> BookModel:
        new_book = BookModel(title=title, author=author)
        self.session.add(new_book)
        await self.session.commit()
        await self.session.refresh(new_book)
        return new_book

    async def get_all_books(self) -> list[BookModel]:
        result = await self.session.execute(select(BookModel))
        return result.scalars().all()