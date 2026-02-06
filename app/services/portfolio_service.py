from sqlalchemy.orm import Session
from app.models import PortfolioItem, MonthlyPlanRequest, MonthlyPlanResponse



def get_portfolio(db: Session):
    """
    Devuelve todo el portfolio desde la base de datos
    """
    return db.query(PortfolioItem).all()
