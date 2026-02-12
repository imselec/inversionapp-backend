# app/services/scoring_service.py

from typing import List, Dict

# Universo permitido (sin SCHD por restricciones en España)
INVESTMENT_UNIVERSE = [
    {"ticker": "AVGO", "sector": "Technology", "score": 92},
    {"ticker": "MSFT", "sector": "Technology", "score": 90},
    {"ticker": "JNJ", "sector": "Healthcare", "score": 88},
    {"ticker": "PG", "sector": "Consumer Defensive", "score": 85},
    {"ticker": "XOM", "sector": "Energy", "score": 82},
    {"ticker": "CVX", "sector": "Energy", "score": 80},
    {"ticker": "JPM", "sector": "Financials", "score": 87},
    {"ticker": "BLK", "sector": "Financials", "score": 84},
    {"ticker": "O", "sector": "REIT", "score": 78},
]

def get_ranked_candidates() -> List[Dict]:
    """
    Devuelve los activos ordenados por score descendente.
    No ejecuta nada externo.
    """
    return sorted(INVESTMENT_UNIVERSE, key=lambda x: x["score"], reverse=True)


def get_top_recommendations(monthly_amount: float = 200) -> Dict:
    """
    Genera una recomendación simple asignando el capital mensual
    al activo con mayor score.
    """

    ranked = get_ranked_candidates()

    if not ranked:
        return {
            "monthly_investment": monthly_amount,
            "recommendations": []
        }

    top_asset = ranked[0]

    return {
        "monthly_investment": monthly_amount,
        "recommendations": [
            {
                "ticker": top_asset["ticker"],
                "sector": top_asset["sector"],
                "score": top_asset["score"],
                "allocated_amount": monthly_amount
            }
        ]
    }
