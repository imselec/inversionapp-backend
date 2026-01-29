from app.services.portfolio_service import load_portfolio

MONTHLY_BUDGET = 200
MAX_WEIGHT = 0.25

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

def portfolio_weights():
    df = load_portfolio()
    if df.empty:
        return {}

    df["value"] = df["shares"] * df["price"]
    total = df["value"].sum()

    return (
        df.groupby("symbol")["value"].sum() / total
    ).to_dict()

def score_asset(weight, price):
    score = 100
    score -= int(weight * 100)
    if price > MONTHLY_BUDGET:
        score -= 40
    return max(score, 0)

def generate_candidates():
    weights = portfolio_weights()
    candidates = []

    for symbol, meta in UNIVERSE.items():
        weight = weights.get(symbol, 0)
        price = meta["price"]

        eligible = True
        reasons = []

        if symbol in EXCLUDED:
            eligible = False
            reasons.append("Excluded asset")

        if weight > MAX_WEIGHT:
            eligible = False
            reasons.append("Overweight in portfolio")

        if price > MONTHLY_BUDGET:
            eligible = False
            reasons.append("Price exceeds monthly budget")

        if not reasons:
            reasons.append("Eligible for recommendation")

        candidates.append({
            "symbol": symbol,
            "sector": meta["sector"],
            "price": price,
            "current_weight": round(weight, 4),
            "eligible": eligible,
            "reasons": reasons,
            "score": score_asset(weight, price)
        })

    return {
        "count": len(candidates),
        "candidates": sorted(
            candidates,
            key=lambda x: x["score"],
            reverse=True
        )
    }
