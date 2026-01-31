from sqlalchemy import Column, Integer, String, Float
from .db import Base

class Portfolio(Base):
    __tablename__ = "portfolio"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    quantity = Column(Float)
    avg_price = Column(Float)
