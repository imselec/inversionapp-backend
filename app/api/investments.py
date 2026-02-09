from fastapi import APIRouter

from app.schemas import (
    MonthlyPlanRequest,
    MonthlyPlanResponse,
    RecommendedBuy,
    PostPurchaseSnapshot
)

router = APIRouter(
    prefix="/investments",
    tags=["Investments"]
)

@router.post("/plan/monthly", response_model=MonthlyPlanResponse)
def generate_monthly_plan(request: MonthlyPlanRequest):
    """
    Genera un plan de inversión mensual simple.
    Más adelante aquí irá la lógica real.
    """

    recommended_buys = [
        RecommendedBuy(
            symbol="MSFT",
            amount_usd=request.monthly_amount * 0.6,
            estimated_shares=1.2
        ),
        RecommendedBuy(
            symbol="O",
            amount_usd=request.monthly_amount * 0.4,
            estimated_shares=2.1
        )
    ]

    snapshot = PostPurchaseSnapshot(
        total_value=2500,
        portfolio_yield=2.8,
        monthly_dividends_estimated=15
    )

    return MonthlyPlanResponse(
        monthly_amount=request.monthly_amount,
        recommended_buys=recommended_buys,
        post_purchase_snapshot=snapshot
    )
