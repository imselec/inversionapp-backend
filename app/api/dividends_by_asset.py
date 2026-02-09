# app/api/dividends_by_asset.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def dividends_by_asset():
    return [
        {"ticker": "UPS", "annual_dividend_usd": 45, "percentage_of_total": 8.3},
        {"ticker": "TXN", "annual_dividend_usd": 35, "percentage_of_total": 6.5},
        {"ticker": "PG", "annual_dividend_usd": 60, "percentage_of_total": 11.0},
        {"ticker": "AVGO", "annual_dividend_usd": 50, "percentage_of_total": 9.2},
        {"ticker": "CVX", "annual_dividend_usd": 85, "percentage_of_total": 15.7},
        {"ticker": "XOM", "annual_dividend_usd": 80, "percentage_of_total": 14.7},
        {"ticker": "ABBV", "annual_dividend_usd": 30, "percentage_of_total": 5.5},
        {"ticker": "LMT", "annual_dividend_usd": 25, "percentage_of_total": 4.6},
        {"ticker": "JNJ", "annual_dividend_usd": 90, "percentage_of_total": 16.7},
        {"ticker": "JPM", "annual_dividend_usd": 20, "percentage_of_total": 3.7},
        {"ticker": "O", "annual_dividend_usd": 95, "percentage_of_total": 17.6},
        {"ticker": "DUK", "annual_dividend_usd": 18, "percentage_of_total": 3.3},
        {"ticker": "KO", "annual_dividend_usd": 50, "percentage_of_total": 9.2},
        {"ticker": "PEP", "annual_dividend_usd": 40, "percentage_of_total": 7.3},
        {"ticker": "NEE", "annual_dividend_usd": 22, "percentage_of_total": 4.0},
    ]
