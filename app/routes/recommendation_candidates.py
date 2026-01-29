from fastapi import APIRouter
from app.services.recommendation_candidates_service import generate_candidates

router = APIRouter(
    prefix="/recommendations/candidates",
    tags=["recommendations"]
)

@router.get("")
def candidates():
    return generate_candidates()
