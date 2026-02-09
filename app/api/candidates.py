# app/api/candidates.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def recommendation_candidates():
    return [
        {"ticker": "JEPI", "reason": "High monthly income via covered calls", "sector": "Multi-Asset"},
    ]
