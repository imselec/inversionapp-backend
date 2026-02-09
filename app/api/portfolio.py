from fastapi import APIRouter
from typing import List

from app.schemas import PortfolioItem

router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"]
)

# Endpoint: snapshot del portfolio
@router.get("/snapshot", response_model=List[PortfolioItem])
def get_portfolio_snapshot():
    """
    Devuelve el estado actual del portfolio.
    En producción esto leerá del CSV o BD.
    """
    return [
        PortfolioItem(
            symbol="AAPL",
            shares=10,
            price_per_share=180,
            total_value=1800,
            yield_percent=0.5,
            sector="Technology"
        ),
        PortfolioItem(
            symbol="JNJ",
            shares=5,
            price_per_share=160,
            total_value=800,
            yield_percent=3.0,
            sector="Healthcare"
        )
    ]


