from fastapi import APIRouter

router = APIRouter(
    prefix="/portfolio",
    tags=["portfolio"]
)

@router.get("/snapshot")
def portfolio_snapshot():
    # Aquí puedes devolver datos reales de tu CSV o servicio
    return {"message": "snapshot data"}

@router.get("/time-series")
def portfolio_time_series():
    return {"message": "time series data"}
