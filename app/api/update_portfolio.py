import os
from fastapi import APIRouter, HTTPException, Header
from app.services.update_portfolio import update_portfolio

router = APIRouter()

@router.post("/update-portfolio")
def update_portfolio_endpoint(secret_key: str = Header(...)):
    if secret_key != os.getenv("SECRET_KEY"):
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    update_portfolio()
    return {"status": "Portfolio actualizado ✅"}
