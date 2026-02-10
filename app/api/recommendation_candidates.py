# app/api/recommendation_candidates.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_recommendation_candidates():
    """
    Retorna los candidatos a recomendaciones (1 usuario).
    """
    return [
        {"ticker": "JEPI", "reason": "High monthly income via covered calls", "sector": "Multi-Asset"},
        {"ticker": "VIG", "reason": "Dividend growth ETF", "sector": "Dividend Growth"},
        {"ticker": "VYM", "reason": "High yield broad exposure", "sector": "High Yield"},
    ]
