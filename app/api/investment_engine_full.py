from fastapi import APIRouter
import pandas as pd
from datetime import datetime

router = APIRouter()

# Configuración
INVESTMENT_MONTHLY = 200
EXCLUDED_TICKERS = ["SCHD"]
CSV_PATH = "app/portfolio.csv"

# --- Recomendaciones ---
@router.get("/investment/recommendations")
def investment_recommendations():
    """
    Genera recomendaciones de compra según portafolio actual.
    No modifica CSV.
    """
    df = pd.read_csv(CSV_PATH)
    df = df[~df["ticker"].isin(EXCLUDED_TICKERS)].copy()
    df["position_value"] = df["shares"] * df["price"]
    total_value = df["position_value"].sum()

    if total_value == 0:
        tickers = df["ticker"].tolist()
        allocation = INVESTMENT_MONTHLY / len(tickers)
        recommendations = [{"ticker": t, "buy_usd": round(allocation,2)} for t in tickers]
    else:
        df["weight"] = df["position_value"] / total_value
        df["buy_usd"] = df["weight"] * INVESTMENT_MONTHLY
        recommendations = [
            {"ticker": row["ticker"], "buy_usd": round(row["buy_usd"],2)}
            for _, row in df.iterrows()
        ]

    return {
        "total_portfolio_value": round(total_valu_
