from fastapi import FastAPI
from app.api.v1.routers import router as v1_router

app = FastAPI()

# Include the v1 router
app.include_router(v1_router, prefix="/api")