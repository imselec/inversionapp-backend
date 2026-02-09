# app/api/history.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def history():
    return [
        {"id": "h1", "run_date": "2026-02-01T10:00:00Z", "invested_amount": 200, "recommendations_count": 4, "pdf_path": None, "email_sent": False}
    ]
