from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app import db, models, services

# Crear tablas si no existen
models.Base.metadata.create_all(bind=db.engine)

app = FastAPI(title="InversionAPP Backend")

# Configurar CORS para Lovable
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

# Dependency para DB
def get_db():
    session = db.SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/system/status")
def status():
    return {"status": "ok"}

@app.get("/portfolio")
def get_portfolio_endpoint(db: Session = Depends(get_db)):
    return services.get_portfolio(db)
