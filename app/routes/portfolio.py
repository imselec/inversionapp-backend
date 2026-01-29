from fastapi import APIRouter
from app.services.portfolio_service import load_portfolio

router = APIRouter(
    prefix="/portfolio",
    tags=["portfolio"]
)

@router.get("/snapshot")
def portfolio_snapshot():
    df = load_portfolio()

    return {
        "assets": [
            {
                "ticker": row["ticker"],
                "quantity": float(row["quantity"])
            }
            for _, row in df.iterrows()
        ],
        "total_assets": len(df)
    }
    
@router.get("/time-series")
def portfolio_time_series():
    from app.services.portfolio_service import load_time_series
    return load_time_series()

@router.get("/dividends-by-asset")
def dividends_by_asset():
    from app.services.portfolio_service import dividends_by_asset
    return dividends_by_asset()

@router.get("/yield-history")
def yield_history():
    from app.services.portfolio_service import yield_history
    return yield_history()


