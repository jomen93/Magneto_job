from fastapi import APIRouter, HTTPException, Depends
from app.services.stats_service import get_stats
from sqlalchemy.orm import Session
from app.core.database import get_db


router = APIRouter()

@router.get("/", name="Statistical info", description="Related with data") 
async def get_statistics(db: Session = Depends(get_db)):
    stats = get_stats()
    return stats
