# app/api/system.py
from fastapi import APIRouter

router = APIRouter()  # Sin prefix aquí

@router.get("/status")
def system_status():
    return {
        "status": "ok",
        "service": "inversionapp-backend"
    }
