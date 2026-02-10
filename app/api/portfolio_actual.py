# app/api/portfolio_actual.py
from fastapi import APIRouter

router = APIRouter()

@router.get("")
def get_portfolio():
    return [
        {"symbol": "UPS", "shares": 0.5577},
        {"symbol": "TXN", "shares": 0.315},
        {"symbol": "PG", "shares": 0.6941},
        {"symbol": "AVGO", "shares": 0.565},
        {"symbol": "CVX", "shares": 1.0876},
        {"symbol": "XOM", "shares": 1.0643},
        {"symbol": "ABBV", "shares": 0.3574},
        {"symbol": "LMT", "shares": 0.2592},
        {"symbol": "JNJ", "shares": 1.0214},
        {"symbol": "JPM", "shares": 0.2303},
        {"symbol": "O", "shares": 1.4206},
        {"symbol": "DUK", "shares": 0.2092},
        {"symbol": "KO", "shares": 0.5996},
        {"symbol": "PEP", "shares": 0.4824},
        {"symbol": "NEE", "shares": 0.2875},
    ]
