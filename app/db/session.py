from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.core.config import settings
from app.db.base import Base  # Import Base for metadata

database_url = (
    "postgresql+asyncpg://" +
    f"{settings.db_username}:{settings.db_password}" +
    f"@{settings.db_host}:{settings.db_port}/{settings.db_name}"
)
engine = create_async_engine(database_url, echo=True)
new_async_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncSession:
    async with new_async_session() as session:
        yield session

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)