from fastapi import APIRouter

router = APIRouter()

@router.get("/alerts")
def alerts():
    return [
        {"ticker": "CVX", "type": "buy", "price": 160},
        {"ticker": "XOM", "type": "sell", "price": 110}
    ]
