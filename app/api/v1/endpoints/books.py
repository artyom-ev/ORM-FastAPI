from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.book import BookSchema, BookGetSchema
from app.db.repositories.book import BookRepository
from app.db.session import get_session

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/", response_model=BookSchema)
async def add_book(book: BookSchema, session: AsyncSession = Depends(get_session)):
    repo = BookRepository(session)
    new_book = await repo.create_book(title=book.title, author=book.author)
    return BookSchema(title=new_book.title, author=new_book.author)

@router.get("/", response_model=list[BookGetSchema])
async def get_books(session: AsyncSession = Depends(get_session)):
    repo = BookRepository(session)
    books = await repo.get_all_books()
    return [BookGetSchema.model_validate(book) for book in books]