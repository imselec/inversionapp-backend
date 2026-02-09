from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def dividends():
    return [
        {"ticker": "UPS", "annual_dividend_usd": 50, "percentage_of_total": 10.4},
        {"ticker": "TXN", "annual_dividend_usd": 25, "percentage_of_total": 5.2},
        {"ticker": "PG", "annual_dividend_usd": 35, "percentage_of_total": 7.3},
        {"ticker": "JNJ", "annual_dividend_usd": 80, "percentage_of_total": 16.7},
        # ... agregar según tu cartera
    ]
