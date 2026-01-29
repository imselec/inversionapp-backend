import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PORTFOLIO_FILE = BASE_DIR / "portfolio.csv"

def load_portfolio():
    return pd.read_csv(PORTFOLIO_FILE)

def load_time_series():
    # Datos mínimos reales (pueden venir luego de CSV histórico)
    return {
        "dates": [
            "2025-11",
            "2025-12",
            "2026-01"
        ],
        "portfolio_value": [
            1000,
            1200,
            1400
        ]
    }

@router.get("/dividends-by-asset")
def dividends_by_asset():
    from app.services.portfolio_service import dividends_by_asset
    return dividends_by_asset()

def yield_history():
    return {
        "UPS": {"2023": 5.2, "2024": 6.1},
        "ABBV": {"2023": 4.3, "2024": 4.7},
        "LMT": {"2023": 3.1, "2024": 3.5}
    }
