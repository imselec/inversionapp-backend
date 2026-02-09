from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Modelo para la solicitud de inversión mensual
class InvestmentRequest(BaseModel):
    monthly_budget: float = 200.0

# Modelo para la respuesta de asignación
class InvestmentAllocation(BaseModel):
    ticker: str
    current_ratio: float  # porcentaje en cartera
    allocation_usd: float

# Cartera actualizada al 2026-02-09
portfolio = [
    {"ticker": "UPS", "ratio": 0.5577},
    {"ticker": "TXN", "ratio": 0.3150},
    {"ticker": "PG",  "ratio": 0.6941},
    {"ticker": "AVGO","ratio": 0.5650},
    {"ticker": "CVX", "ratio": 1.0876},
    {"ticker": "XOM", "ratio": 1.0643},
    {"ticker": "ABBV","ratio": 0.3574},
    {"ticker": "LMT", "ratio": 0.2592},
    {"ticker": "JNJ", "ratio": 1.0214},
    {"ticker": "JPM", "ratio": 0.2303},
    {"ticker": "O",   "ratio": 1.4206},
    {"ticker": "DUK", "ratio": 0.2092},
    {"ticker": "KO",  "ratio": 0.5996},
    {"ticker": "PEP", "ratio": 0.4824},
    {"ticker": "NEE", "ratio": 0.2875},
]

@router.post("/plan/monthly", response_model=List[InvestmentAllocation])
def monthly_investment_plan(request: InvestmentRequest):
    total_ratio = sum([p["ratio"] for p in portfolio])
    allocations = []

    for p in portfolio:
        allocation = (p["ratio"] / total_ratio) * request.monthly_budget
        allocations.append(
            InvestmentAllocation(
                ticker=p["ticker"],
                current_ratio=p["ratio"],
                allocation_usd=round(allocation, 2)
            )
        )

    return allocations
