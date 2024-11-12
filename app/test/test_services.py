# app/test/test_services.py

from app.services.mutant_detector import MutantDetectorService
from app.services.stats_service import get_stats
from unittest.mock import MagicMock
from app.models.dna_sequence import DNASequence

def test_is_mutant_service():
    # Crea una instancia de MutantDetectorService con mock_db
    mock_db = MagicMock()
    detector = MutantDetectorService(mock_db)
    
    # Prueba con ADN mutante
    mutant_dna = ["ACACGG", "CAGTGC", "ATATGT", "TGATGT", "CACATA", "TGACTG"]
    assert detector.is_mutant(mutant_dna) == True
    
    # Prueba con ADN no mutante
    human_dna = ["ATCGAA", "CGTAGC", "TCAAGG", "GGTACA", "CTAGTA", "AGCTAG"]
    assert detector.is_mutant(human_dna) == False

def test_get_stats_service():
    # Mockeando la base de datos y el método de stats
    mock_db = MagicMock()
    
    # Configura el mock para simular el número de secuencias mutantes y humanas
    mock_db.query(DNASequence).filter(DNASequence.is_mutant == True).count.return_value = 40
    mock_db.query(DNASequence).filter(DNASequence.is_mutant == False).count.return_value = 100
    
    # Llama a get_stats con el mock_db
    stats = get_stats(mock_db)
    
    # Verifica que los campos de estadísticas están presentes y con valores esperados
    assert "count_mutant_dna" in stats
    assert "count_human_dna" in stats
    assert "ratio" in stats
    assert stats["count_mutant_dna"] == 100
    assert stats["count_human_dna"] == 100
    assert stats["ratio"] == 1

