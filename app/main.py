# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.recommendations import router as recommendations_router

app = FastAPI(
    title="InversionAPP Backend",
    version="2.0.0"
)

# CORS abierto para Lovable / Render
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(
    recommendations_router,
    prefix="/recommendations",
    tags=["recommendations"]
)

@app.get("/")
def root():
    return {"status": "ok", "service": "InversionAPP Backend"}

@app.get("/system/status")
def system_status():
    return {"status": "running"}
