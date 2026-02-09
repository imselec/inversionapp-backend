from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def recommendations():
    return [
        {"ticker": "SCHD", "allocation_usd": 80, "yield": 3.5, "reason": "Strong dividend growth history", "score": 92},
        {"ticker": "VYM", "allocation_usd": 60, "yield": 3.1, "reason": "Broad high-yield exposure", "score": 88},
    ]
