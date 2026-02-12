from pathlib import Path
from typing import List, Dict
import csv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PORTFOLIO_FILE = BASE_DIR / "portfolio.csv"

# Mapa simple ticker → sector
SECTOR_MAP = {
    "AVGO": "Technology",
    "MSFT": "Technology",
    "JNJ": "Healthcare",
    "PG": "Consumer Defensive",
    "XOM": "Energy",
    "CVX": "Energy",
    "JPM": "Financials",
    "BLK": "Financials",
    "O": "REIT",
}


def load_portfolio() -> List[Dict]:
    if not PORTFOLIO_FILE.exists():
        return []

    portfolio = []

    try:
        with open(PORTFOLIO_FILE, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ticker = row["ticker"]
                shares = float(row["shares"])
                avg_price = float(row["avg_price"])
                market_value = shares * avg_price

                portfolio.append({
                    "ticker": ticker,
                    "shares": shares,
                    "avg_price": avg_price,
                    "market_value": market_value,
                    "sector": SECTOR_MAP.get(ticker, "Unknown")
                })
    except Exception:
        return []

    return portfolio


def calculate_sector_weights() -> Dict[str, float]:
    """
    Devuelve peso porcentual por sector.
    """
    portfolio = load_portfolio()

    if not portfolio:
        return {}

    total_value = sum(p["market_value"] for p in portfolio)

    sector_totals = {}

    for p in portfolio:
        sector = p["sector"]
        sector_totals[sector] = sector_totals.get(sector, 0) + p["market_value"]

    sector_weights = {
        sector: (value / total_value) * 100
        for sector, value in sector_totals.items()
    }

    return sector_weights
