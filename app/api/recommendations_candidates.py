from fastapi import APIRouter

router = APIRouter(
    prefix="/recommendations",
    tags=["recommendations"]
)

@router.get("/candidates")
def get_recommendation_candidates():
    return {
        "candidates": [
            {
                "symbol": "JPM",
                "reason": "High quality bank with strong dividends"
            },
            {
                "symbol": "MS",
                "reason": "Investment bank with growing yield"
            },
            {
                "symbol": "O",
                "reason": "REIT aligned with monthly income strategy"
            }
        ]
    }
