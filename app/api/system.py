from fastapi import APIRouter

router = APIRouter()

@router.get("/system/status")
def system_status():
    return {"status": "ok"}
