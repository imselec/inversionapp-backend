from app.services.portfolio_service import load_portfolio

MONTHLY_BUDGET = 200

UNIVERSE = {
    "PG": {"sector": "defensive", "price": 150},
    "KO": {"sector": "defensive", "price": 60},
    "PEP": {"sector": "defensive", "price": 170},
    "MSFT": {"sector": "tech", "price": 380},
    "TXN": {"sector": "tech", "price": 170},
    "AAPL": {"sector": "tech", "price": 190},
    "ENB": {"sector": "energy", "price": 36},
    "SHEL": {"sector": "energy", "price": 65},
}

EXCLUDED = {"SCHD"}

def current_weights():
    df = load_portfolio()
    if df.empty:
        return {}

    df["value"] = df["shares"] * df["price"]
    total = df["value"].sum()

    weights = (
        df.groupby("symbol")["value"]
        .sum() / total
    ).to_dict()

    return weights

def generate_recommendations():
    weights = current_weights()
    recommendations = []

    remaining = MONTHLY_BUDGET

    for symbol, meta in UNIVERSE.items():
        if symbol in EXCLUDED:
            continue

        weight = weights.get(symbol, 0)

        if weight > 0.25:
            continue  # sobreponderado

        price = meta["price"]

        if price > remaining:
            continue

        shares = round(remaining // price, 2)
        if shares <= 0:
            continue

        recommendations.append({
            "symbol": symbol,
            "shares": shares,
            "estimated_cost": round(shares * price, 2),
            "sector": meta["sector"]
        })

        remaining -= shares * price

        if remaining < 50:
            break

        if len(recommendations) == 3:
            break

    return {
        "budget": MONTHLY_BUDGET,
        "used": round(MONTHLY_BUDGET - remaining, 2),
        "remaining": round(remaining, 2),
        "recommendations": recommendations
    }
