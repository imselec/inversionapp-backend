from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def time_series():
    return [
        {"date": "2025-09-01", "estimated_annual_dividends": 320, "total_invested": 8000, "average_yield": 4.0},
        {"date": "2025-12-01", "estimated_annual_dividends": 420, "total_invested": 8800, "average_yield": 4.3},
        {"date": "2026-02-01", "estimated_annual_dividends": 482, "total_invested": 9600, "average_yield": 4.5},
    ]
