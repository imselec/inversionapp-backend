from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app import db, models, services

# Crear tablas si no existen
models.Base.metadata.create_all(bind=db.engine)

app = FastAPI(title="InversionAPP Backend")

# CORS para Lovable
origins = [
    "https://lovable.ai",
    "http://localhost",
    "http://127.0.0.1"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency DB
def get_db():
    session = db.SessionLocal()
    try:
        yield session
    finally:
        session.close()

# Status
@app.get("/system/status")
def status():
    return {"status": "ok"}

# Portfolio desde DB
@app.get("/portfolio")
def get_portfolio_endpoint(db: Session = Depends(get_db)):
    assets = db.query(models.Portfolio).all()
    result = []
    for asset in assets:
        result.append({
            "symbol": asset.symbol,
            "quantity": asset.quantity,
            "avg_price": asset.avg_price
        })
    return result

import os
from fastapi import Header, HTTPException

from app import update_portfolio  # el script que creamos

# Endpoint seguro para actualizar portfolio desde CSV
@app.post("/update-portfolio")
def update_portfolio_endpoint(secret_key: str = Header(...)):
    # Validar clave
    if secret_key != os.getenv("SECRET_KEY"):
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Ejecutar actualización
    try:
        update_portfolio.update_portfolio()
        return {"status": "Portfolio actualizado ✅"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
