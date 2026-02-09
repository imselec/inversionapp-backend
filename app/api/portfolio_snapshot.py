from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_snapshot():
    return {
        "date": "2026-02-09",
        "monthly_budget": 200,
        "total_positions": 15,
        "estimated_annual_dividends": 482.50,
        "average_yield": 3.85,
        "holdings": [
            {"symbol": "UPS", "shares": 0.5577},
            {"symbol": "TXN", "shares": 0.3150},
            {"symbol": "PG", "shares": 0.6941},
            {"symbol": "AVGO", "shares": 0.5650},
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
    }
