from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base  # Import Base from the shared location

class BookModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]