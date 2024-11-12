from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.api.routes import mutant, stats
from fastapi.templating import Jinja2Templates


router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_welcome(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})

router.include_router(mutant.router, prefix="/mutant", tags=["mutant"])
router.include_router(stats.router, prefix="/stats", tags=["stats"])
