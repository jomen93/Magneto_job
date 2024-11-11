from fastapi import APIRouter, HTTPException
from app.services.stats_service import get_stats


router = APIRouter()


@router.get("/", name="Statistical info", description="Related with data") 
async def get_statistics():
    stats = get_stats()
    return stats
