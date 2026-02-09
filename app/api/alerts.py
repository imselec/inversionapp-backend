# app/api/alerts.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def alerts():
    return [
        {"id": "a1", "ticker": "AAPL", "signal_type": "HOLD", "indicator": "RSI neutral at 52", "date": "2026-02-09"}
    ]
