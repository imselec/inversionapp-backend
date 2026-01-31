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
