from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON
from sqlalchemy.sql import func
from app.core.database import Base

class DNASequence(Base):
    __tablename__ = "dna_sequences"

    id = Column(Integer, primary_key=True, index=True)
    sequence = Column(String(4096), unique=True, index=True)
    is_mutant = Column(Boolean, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    sequence_length = Column(Integer, nullable=False)
    mutant_sequence_count = Column(Integer, default=0)
    human_sequence_count = Column(Integer, default=0)
    detected_patterns = Column(JSON, nullable=True)
