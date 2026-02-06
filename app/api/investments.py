from fastapi import APIRouter
from app.models import MonthlyPlanRequest, MonthlyPlanResponse
from app.services.investment_planner import generate_monthly_plan

router = APIRouter()

@router.post("/plan/monthly", response_model=MonthlyPlanResponse)
def plan_monthly(request: MonthlyPlanRequest):
    return generate_monthly_plan(request)
