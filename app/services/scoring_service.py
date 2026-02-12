from typing import List, Dict
from app.services.portfolio_service import (
    load_portfolio,
    calculate_sector_weights
)
from app.services.config_service import load_config

INVESTMENT_UNIVERSE = [
    {"ticker": "AVGO", "sector": "Technology", "base_score": 92},
    {"ticker": "MSFT", "sector": "Technology", "base_score": 90},
    {"ticker": "JNJ", "sector": "Healthcare", "base_score": 88},
    {"ticker": "PG", "sector": "Consumer Defensive", "base_score": 85},
    {"ticker": "XOM", "sector": "Energy", "base_score": 82},
    {"ticker": "CVX", "sector": "Energy", "base_score": 80},
    {"ticker": "JPM", "sector": "Financials", "base_score": 87},
    {"ticker": "BLK", "sector": "Financials", "base_score": 84},
    {"ticker": "O", "sector": "REIT", "base_score": 78},
]


def get_ranked_candidates() -> List[Dict]:
    config = load_config()
    benchmark = config.get("benchmark", {})

    portfolio = load_portfolio()
    owned_tickers = {p["ticker"] for p in portfolio}
    sector_weights = calculate_sector_weights()

    adjusted = []

    for asset in INVESTMENT_UNIVERSE:
        score = asset["base_score"]
        sector = asset["sector"]

        current_weight = sector_weights.get(sector, 0)
        benchmark_weight = benchmark.get(sector, 0)

        # Penalización por ya poseer
        if asset["ticker"] in owned_tickers:
            score -= 2

        deviation = current_weight - benchmark_weight

        if deviation > 0:
            score -= deviation * 0.4
        else:
            score += abs(deviation) * 0.15

        adjusted.append({
            "ticker": asset["ticker"],
            "sector": sector,
            "score": round(score, 2),
            "portfolio_sector_weight": round(current_weight, 2),
            "benchmark_sector_weight": benchmark_weight,
            "deviation_vs_benchmark": round(deviation, 2)
        })

    return sorted(adjusted, key=lambda x: x["score"], reverse=True)


def get_top_recommendations(monthly_amount: float = None) -> Dict:
    config = load_config()

    if monthly_amount is None:
        monthly_amount = config.get("monthly_investment", 200)

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
                "portfolio_sector_weight": top_asset["portfolio_sector_weight"],
                "benchmark_sector_weight": top_asset["benchmark_sector_weight"],
                "deviation_vs_benchmark": top_asset["deviation_vs_benchmark"],
                "allocated_amount": monthly_amount
            }
        ]
    }
