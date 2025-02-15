from fastapi import APIRouter
from app.api.v1.endpoints.books import router as books_router
from app.api.v1.endpoints.setup import router as setup_router

router = APIRouter(prefix="/v1")  # Prefix for all v1 routes

# Include all endpoint routers
router.include_router(books_router)
router.include_router(setup_router)