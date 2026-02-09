from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def recommendations():
    return [
        {"ticker": "VYM", "allocation_usd": 100, "yield": 3.1, "reason": "Diversified high yield", "score": 88},
        {"ticker": "JEPI", "allocation_usd": 80, "yield": 3.5, "reason": "Covered calls monthly income", "score": 92},
    ]
