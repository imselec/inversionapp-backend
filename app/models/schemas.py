from pydantic import BaseModel
from typing import List, Optional

# =====================
# Portfolio
# =====================
class PortfolioItem(BaseModel):
    symbol: str
    shares: float
    price_per_share: float
    total_value: float
    yield_percent: Optional[float] = None  # dividend yield
    sector: Optional[str] = None

# =====================
# Input del plan mensual
# =====================
class PlanConstraints(BaseModel):
    exclude_assets: Optional[List[str]] = []
    max_weight_per_asset: Optional[float] = 0.2  # 0.2 = 20%

class MonthlyPlanRequest(BaseModel):
    monthly_amount: float = 200
    currency: str = "USD"
    strategy: Optional[str] = "dividend_growth"
    constraints: Optional[PlanConstraints] = PlanConstraints()

# =====================
# Output del plan mensual
# =====================
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
