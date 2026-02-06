from pydantic import BaseModel

class PortfolioItemSchema(BaseModel):
    symbol: str
    shares: float
    price: float

    class Config:
        orm_mode = True
