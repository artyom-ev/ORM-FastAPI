from fastapi import APIRouter
from app.db.session import init_db

router = APIRouter(prefix="/setup", tags=["setup"])

@router.post("/")
async def setup_database():
    await init_db()
    return {"message": "Database initialized"}