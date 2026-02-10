from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.services.monthly_plan_engine import build_monthly_plan
import requests

router = APIRouter()

class PlanRequest(BaseModel):
    amount: float
    strategy: str
    exclude: List[str] = []

@router.post("/")
def monthly_plan(body: PlanRequest):
    # Traer holdings actuales
    portfolio = requests.get("https://inversionapp-backend.onrender.com/portfolio").json()
    # Traer recomendaciones
    recommendations = requests.get("https://inversionapp-backend.onrender.com/recommendations").json()
    
    result = build_monthly_plan(body.amount, body.strategy, body.exclude, portfolio, recommendations)
    return result
