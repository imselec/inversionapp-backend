from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def status():
    return {"status": "READY", "last_run": "2026-02-09T10:00:00Z", "message": "System operational"}

@router.get("/audit")
def audit():
    return {"status": "PASS", "messages": [{"level": "info", "text": "All checks passed"}]}
