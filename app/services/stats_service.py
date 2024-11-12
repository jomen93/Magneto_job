from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.dna_sequence import DNASequence

def get_stats(db: Session):

    number_mutant_dna = db.query(DNASequence).filter(
        DNASequence.is_mutant == True
    ).count()

    number_human_dna = db.query(DNASequence).filter(
        DNASequence.is_mutant == False
    ).count()

    ratio = number_mutant_dna / number_mutant_dna if number_human_dna > 0 else 0

    return {
        "count_mutant_dna": number_mutant_dna,
        "count_human_dna": number_human_dna,
        "ratio": ratio
    }
