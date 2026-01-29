from fastapi import APIRouter
from app.services.recommendation_service import generate_recommendations

router = APIRouter(prefix="/recommendations", tags=["recommendations"])

@router.get("")
def recommendations():
    return generate_recommendations()
