import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import router
from app.core.database import get_db

app = FastAPI(
    title="Magneto Job",
    description="API to find out if it's an X men",
    version="0.0.3 - Born a Hero"
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvircorn.run("app.main:app", host="0.0.0.0", port=port)
# uvircorn main:app --reload
