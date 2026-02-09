# app/api/portfolio_time_series.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def portfolio_time_series():
    return [
        {"date": "2025-09-01", "estimated_annual_dividends": 320, "total_invested": 8000, "average_yield": 4.0},
        {"date": "2025-10-01", "estimated_annual_dividends": 350, "total_invested": 8200, "average_yield": 4.1},
        {"date": "2025-11-01", "estimated_annual_dividends": 380, "total_invested": 8400, "average_yield": 4.2},
        {"date": "2025-12-01", "estimated_annual_dividends": 420, "total_invested": 8800, "average_yield": 4.3},
        {"date": "2026-01-01", "estimated_annual_dividends": 450, "total_invested": 9200, "average_yield": 4.4},
        {"date": "2026-02-01", "estimated_annual_dividends": 482, "total_invested": 9600, "average_yield": 4.5},
    ]
