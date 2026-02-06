from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.db import get_db
from app.services.portfolio_service import get_portfolio
from app.schemas import PortfolioItemSchema

router = APIRouter()

@router.get(
    "/portfolio",
    response_model=list[PortfolioItemSchema]
)
def portfolio_endpoint(db: Session = Depends(get_db)):
    return get_portfolio(db)
