from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from app.services.mutant_detector import MutantDetectorService


router = APIRouter()

# Modelo de entrada
class DNAModel(BaseModel):
    dna: List[str]  # Tipo de datos correcto


@router.post("/", name="DNA info", description="Return is Mutant") 
async def is_mutant(dna_model: DNAModel):
    detector = MutantDetectorService()
    is_mutant = detector.is_mutant(dna_model.dna)

    if is_mutant:
        return {"message": "Mutant detected"}
    else:
        raise HTTPException(status_code=403, detail="Forbidden: Regular human")

