# app/api/investments_plan.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class PlanRequest(BaseModel):
    amount: float = 200
    strategy: str = "dividend_growth"
    exclude: List[str] = []

@router.post("/")
def monthly_plan(body: PlanRequest):
    return {
        "investment_amount": body.amount,
        "strategy": body.strategy,
        "purchases": [
            {"ticker": "VYM", "amount_usd": 100, "shares_to_buy": 0.85, "reason": "High yield diversified ETF"},
            {"ticker": "JNJ", "amount_usd": 100, "shares_to_buy": 0.62, "reason": "Dividend aristocrat, healthcare sector"},
        ],
        "projected_portfolio": [
            {"symbol": "AAPL", "shares": 10, "total_value": 1800},
            {"symbol": "JNJ", "shares": 5.62, "total_value": 899.2},
            {"symbol": "VYM", "shares": 0.85, "total_value": 100},
        ]
    }
