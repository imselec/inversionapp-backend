# app/api/yield_history.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def yield_history():
    return [
        {"date": "2025-09-01", "yield": 3.8},
        {"date": "2025-12-01", "yield": 4.0},
        {"date": "2026-02-01", "yield": 4.2},
    ]
