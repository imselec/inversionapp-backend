# app/api/recommendation_candidates.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def recommendation_candidates():
    """
    Lista de tickers candidatos para nuevas inversiones.
    """
    return [
        {
            "ticker": "JEPI",
            "reason": "High monthly income via covered calls",
            "sector": "Multi-Asset"
        },
        {
            "ticker": "VYM",
            "reason": "Broad high-yield exposure",
            "sector": "ETF"
        },
        {
            "ticker": "PG",
            "reason": "Stable consumer goods dividend",
            "sector": "Consumer"
        },
    ]
