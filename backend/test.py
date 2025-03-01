import asyncio
from database import get_session
from crud import setup_database, add_book, get_books
from schemas import BookSchema

async def main():
    # Initialize the database (only needed once)
    # await setup_database()

    async for session in get_session():  # Use async for to get the session
        # Add a new book
        # new_book = BookSchema(title="Example Book", author="John Doe")
        # created_book = await add_book(new_book, session)
        # print(f"Added Book: {created_book}")

        # Fetch all books
        books = await get_books(session)
        for book in books:
            print(book)

if __name__ == "__main__":
    asyncio.run(main())