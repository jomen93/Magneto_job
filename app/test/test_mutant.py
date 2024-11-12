# app/test/test_mutant.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_mutant_route_with_mutant_dna():
    dna_data = {"dna": ["ACACGG", "CAGTGC", "ATATGT", "TGATGT", "CACATA", "TGACTG"]}
    response = client.post("/mutant/", json=dna_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Mutant detected"}

def test_mutant_route_with_human_dna():
    dna_data = {"dna": ["ATCGAA", "CGTAGC", "TCAAGG", "GGTACA", "CTAGTA", "AGCTAG"]}
    response = client.post("/mutant/", json=dna_data)
    assert response.status_code == 403
    assert response.json() == {'detail': 'Forbidden: Regular human'}

