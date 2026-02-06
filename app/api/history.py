from fastapi import APIRouter

router = APIRouter()

@router.get("/history")
def history():
    return [
        {"date": "2026-01-01", "action": "buy", "ticker": "UPS", "amount": 0.5577},
        {"date": "2026-01-02", "action": "buy", "ticker": "ABBV", "amount": 0.3574},
        {"date": "2026-01-03", "action": "buy", "ticker": "LMT", "amount": 0.1966}
    ]
