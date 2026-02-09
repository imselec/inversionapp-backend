from fastapi import APIRouter
import pandas as pd

router = APIRouter()

# Configuración de inversión
INVESTMENT_MONTHLY = 200
EXCLUDED_TICKERS = ["SCHD"]  # no invertir

@router.get("/investment/recommendations")
def investment_recommendations():
    """
    Motor de inversión: asigna los 200 USD mensuales a los activos existentes,
    excluyendo los prohibidos, y genera sugerencias de compra.
    """
    # Cargar CSV de portafolio
    df = pd.read_csv("app/portfolio.csv")

    # Filtrar activos excluidos
    df = df[~df["ticker"].isin(EXCLUDED_TICKERS)]

    # Valor total actual del portafolio
    df["position_value"] = df["shares"] * df["price"]
    total_value = df["position_value"].sum()

    if total_value == 0:
        # Portafolio vacío, invertir todo proporcional a la cantidad de tickers
        tickers = df["ticker"].tolist()
        allocation = INVESTMENT_MONTHLY / len(tickers)
        return {
            "total_portfolio_value": 0,
            "recommendations": [
                {"ticker": t, "buy_usd": round(allocation, 2)} for t in tickers
            ]
        }

    # Proporción de cada activo
    df["weight"] = df["position_value"] / total_value

    # Calcular recomendación: proporcional al peso actual
    df["buy_usd"] = df["weight"] * INVESTMENT_MONTHLY

    recommendations = [
        {
            "ticker": row["ticker"],
            "buy_usd": round(row["buy_usd"], 2)
        }
        for _, row in df.iterrows()
    ]

    return {
        "total_portfolio_value": round(total_value, 2),
        "recommendations": recommendations
    }

