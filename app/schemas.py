from pydantic import BaseModel
from typing import List, Optional

# =====================================================
# Portfolio
# =====================================================

class PortfolioItem(BaseModel):
    symbol: str
    shares: float
    price_per_share: float
    total_value: float
    yield_percent: Optional[float] = None
    sector: Optional[str] = None


# =====================================================
# Plan mensual - INPUT
# =====================================================

class PlanConstraints(BaseModel):
    exclude_assets: List[str] = []
    max_weight_per_asset: float = 0.2  # 20% por activo


class MonthlyPlanRequest(BaseModel):
    monthly_amount: float = 200
    currency: str = "USD"
    strategy: str = "dividend_growth"
    constraints: Optional[PlanConstraints] = None


# =====================================================
# Plan mensual - OUTPUT
# =====================================================

class RecommendedBuy(BaseModel):
    symbol: str
    amount_usd: float
    estimated_shares: float


class PostPurchaseSnapshot(BaseModel):
    total_value: float
    portfolio_yield: float
    monthly_dividends_estimated: float


class MonthlyPlanResponse(BaseModel):
    monthly_amount: float
    recommended_buys: List[RecommendedBuy]
    post_purchase_snapshot: PostPurchaseSnapshot
