# app/api/portfolio_actual.py
from fastapi import APIRouter
from typing import List

router = APIRouter()

@router.get("/")
def portfolio_actual():
    """
    Devuelve las posiciones actuales del usuario.
    Formato esperado por el frontend para el Plan Mensual real.
    """
    return [
        {
            "symbol": "AAPL",
            "shares": 10,
            "price_per_share": 180,
            "total_value": 1800,
            "yield_percent": 0.5,
            "sector": "Technology"
        },
        {
            "symbol": "JNJ",
            "shares": 5,
            "price_per_share": 160,
            "total_value": 800,
            "yield_percent": 3.0,
            "sector": "Healthcare"
        },
        {
            "symbol": "VYM",
            "shares": 1,
            "price_per_share": 120,
            "total_value": 120,
            "yield_percent": 3.1,
            "sector": "ETF"
        },
    ]
