from fastapi import APIRouter
import pandas as pd
from datetime import datetime

router = APIRouter()

# Configuración
INVESTMENT_MONTHLY = 200
EXCLUDED_TICKERS = ["SCHD"]

@router.post("/investment/apply")
def apply_monthly_investment():
    """
    Aplica la inversión mensual de 200 USD al portafolio.
    Actualiza el CSV con nuevas compras proporcionales.
    """

    # Cargar CSV
    df = pd.read_csv("app/portfolio.csv")

    # Filtrar activos excluidos
    df = df[~df["ticker"].isin(EXCLUDED_TICKERS)].copy()

    # Calcular valor actual y proporciones
    df["position_value"] = df["shares"] * df["price"]
    total_value = df["position_value"].sum()

    if total_value == 0:
        # Portafolio vacío: repartir inversión equitativamente
        tickers = df["ticker"].tolist()
        allocation = INVESTMENT_MONTHLY / len(tickers)
        new_shares = []
        for t in tickers:
            price = df.loc[df["ticker"] == t, "price"].iloc[0]
            shares_to_buy = allocation / price
            new_shares.append({"ticker": t, "shares": shares_to_buy})
    else:
        # Proporción de cada activo
        df["weight"] = df["position_value"] / total_value
        df["buy_usd"] = df["weight"] * INVESTMENT_MONTHLY
        new_shares = []
        for _, row in df.iterrows():
            shares_to_buy = row["buy_usd"] / row["price"]
            new_shares.append({"ticker": row["ticker"], "shares": shares_to_buy})

    # Actualizar CSV
    today = datetime.today().strftime("%Y-%m-%d")
    updates = []
    for ns in new_shares:
        ticker = ns["ticker"]
        shares = ns["shares"]
        price = df.loc[df["ticker"] == ticker, "price"].iloc[0]
        dividend = 0  # inicializar dividendos nuevos como 0
        # Añadir nueva fila al CSV
        updates.append({
            "date": today,
            "ticker": ticker,
            "shares": shares,
            "price": price,
            "dividend": dividend
        })

    # Convertir a DataFrame y append
    df_new = pd.DataFrame(updates)
    df_csv = pd.read_csv("app/portfolio.csv")
    df_csv = pd.concat([df_csv, df_new], ignore_index=True)
    df_csv.to_csv("app/portfolio.csv", index=False)

    return {
        "message": f"Inversión de {INVESTMENT_MONTHLY} USD aplicada correctamente.",
        "details": updates
    }
