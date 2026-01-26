from fastapi import APIRouter

router = APIRouter(
    prefix="/portfolio",
    tags=["portfolio"]
)

@router.get("/snapshot")
def snapshot():
    return {"message": "portfolio snapshot placeholder"}
