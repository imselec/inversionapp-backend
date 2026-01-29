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
