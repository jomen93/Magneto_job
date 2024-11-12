from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import router
from app.core.database import get_db

app = FastAPI(
    title="Magneto Job",
    description="API to find out if it's an X men",
    version="0.0.1 - Born a Hero"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(router)
# uvircorn main:app --reload
