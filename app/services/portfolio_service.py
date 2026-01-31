from sqlalchemy.orm import Session
from app import models

def get_portfolio(db: Session):
    return db.query(models.Portfolio).all()

def add_asset(db: Session, symbol: str, quantity: float, avg_price: float):
    asset = models.Portfolio(symbol=symbol, quantity=quantity, avg_price=avg_price)
    db.add(asset)
    db.commit()
    db.refresh(asset)
    return asset
