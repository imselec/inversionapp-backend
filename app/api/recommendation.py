from fastapi import APIRouter

router = APIRouter()

@router.get("/recommendations")
def recommendations():
    return [
        {"ticker": "PEP", "score": 0.8},
        {"ticker": "TXN", "score": 0.75},
        {"ticker": "JPM", "score": 0.7}
    ]

@router.get("/recommendations/candidates")
def recommendation_candidates():
    return ["PEP", "TXN", "JPM", "CVX"]
