from fastapi import APIRouter

router = APIRouter(
    prefix="/portfolio",
    tags=["portfolio"]
)

@router.get("/snapshot")
def get_snapshot():
    return {
        "O": 0.5,
        "CVX": 1.0,
        "BMY": 0.0,
        "XOM": 1.0,
        "PG": 0.0,
        "KO": 0.0,
        "JNJ": 1.0,
        "CSCO": 0.0,
        "MSFT": 0.0,
        "AVGO": 0.35,
        "LMT": 0.1966,
        "UPS": 0.5577,
        "ABBV": 0.3574
    }

@router.get("/time-series")
def get_time_series():
    return {
        "dates": ["2026-01-01", "2026-01-02", "2026-01-03"],
        "O": [0.5, 0.52, 0.53],
        "CVX": [1.0, 1.01, 1.02],
        "UPS": [0.55, 0.56, 0.57]
    }

@router.get("/dividends-by-asset")
def dividends_by_asset():
    return {
        "UPS": 12.4,
        "ABBV": 18.9,
        "LMT": 9.1
    }

@router.get("/yield-history")
def yield_history():
    return {
        "dates": ["2025-12-01", "2025-12-02", "2025-12-03"],
        "total_yield": [100, 101, 102]
    }

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

@router.get("/alerts")
def alerts():
    return [
        {"ticker": "CVX", "type": "buy", "price": 160},
        {"ticker": "XOM", "type": "sell", "price": 110}
    ]

@router.get("/history")
def history():
    return [
        {"date": "2026-01-01", "action": "buy", "ticker": "UPS", "amount": 0.5577},
        {"date": "2026-01-02", "action": "buy", "ticker": "ABBV", "amount": 0.3574},
        {"date": "2026-01-03", "action": "buy", "ticker": "LMT", "amount": 0.1966}
    ]
