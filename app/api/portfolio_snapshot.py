from fastapi import APIRouter
from datetime import date

router = APIRouter()

@router.get("/")
def portfolio_snapshot():
    """
    Devuelve el snapshot del portafolio.
    """
    return {
        "date": str(date.today()),
        "monthly_budget": 200,
        "total_positions": 15,
        "estimated_annual_dividends": 482.50,
        "average_yield": 3.85
    }
