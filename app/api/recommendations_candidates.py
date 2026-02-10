from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

# Lista de candidatos (puedes expandir según estrategia)
CANDIDATES = [
    {"ticker": "JEPI", "reason": "High monthly income via covered calls", "sector": "Multi-Asset"},
    {"ticker": "VIG", "reason": "Stable dividend growth ETF", "sector": "US Equity"},
    {"ticker": "SCHD", "reason": "Strong dividend history", "sector": "US Equity"}
]

@router.get("/recommendations/candidates")
def get_candidates():
    return JSONResponse(content=CANDIDATES)
