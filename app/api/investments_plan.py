from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class MonthlyPlanRequest(BaseModel):
    amount: float = 200
    strategy: str = "dividend_growth"
    exclude: List[str] = []

@router.post("/monthly")
def generate_monthly_plan(body: MonthlyPlanRequest):
    return {
        "investment_amount": body.amount,
        "strategy": body.strategy,
        "purchases": [
            {
                "ticker": "VYM",
                "amount_usd": 100,
                "shares_to_buy": 0.85,
                "reason": "High dividend yield ETF"
            },
            {
                "ticker": "JNJ",
                "amount_usd": 100,
                "shares_to_buy": 0.62,
                "reason": "Dividend aristocrat healthcare stock"
            }
        ]
    }
