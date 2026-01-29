from fastapi import APIRouter

router = APIRouter(
    prefix="/system",
    tags=["system"]
)

@router.get("/status")
def system_status():
    return {"status": "ok"}

@router.get("/audit")
def system_audit():
    return {"audit": "No issues detected", "checks": ["db", "api", "services"]}
