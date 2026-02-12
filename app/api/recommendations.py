# app/api/recommendations.py

from fastapi import APIRouter, Query
from app.services.scoring_service import (
    get_ranked_candidates,
    get_top_recommendations
)

router = APIRouter()


@router.get("/candidates")
def candidates():
    """
    Devuelve todos los activos ordenados por score.
    """
    return {
        "candidates": get_ranked_candidates()
    }


@router.get("/monthly")
def monthly_recommendation(
    amount: float = Query(default=200, ge=50, le=10000)
):
    """
    Devuelve la recomendación mensual.
    """
    return get_top_recommendations(monthly_amount=amount)
