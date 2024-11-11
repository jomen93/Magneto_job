from fastapi import APIRouter
from app.api.routes import mutant, stats

router = APIRouter()

router.include_router(mutant.router, prefix="/mutant", tags=["mutant"])
router.include_router(stats.router, prefix="/stats", tags=["stats"])
