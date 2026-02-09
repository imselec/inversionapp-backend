# app/api/system_status.py
from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/")
def system_status():
    return {
        "status": "READY",
        "last_run": datetime.utcnow().isoformat(),
        "message": "System operational"
    }
