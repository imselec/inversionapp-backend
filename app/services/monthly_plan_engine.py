def build_monthly_plan(monthly_amount: float, strategy: str, exclude: list, current_portfolio: list, recommendations: list):
    purchases = []
    remaining_amount = monthly_amount

    # Filtrar recomendaciones
    candidates = [r for r in recommendations if r["ticker"] not in exclude]

    for r in candidates:
        ticker = r["ticker"]
        price = next((p["price_per_share"] for p in current_portfolio if p["symbol"] == ticker), None)
        if price is None:
            price = 100  # fallback: precio estimado si no existe
        buy_amount = remaining_amount / len(candidates)
        shares_to_buy = round(buy_amount / price, 2)
        purchases.append({
            "ticker": ticker,
            "amount_usd": buy_amount,
            "shares_to_buy": shares_to_buy,
            "reason": r.get("reason", "Recommended by system")
        })
        remaining_amount -= buy_amount

    # Generar portafolio proyectado
    projected = current_portfolio.copy()
    for p in purchases:
        found = next((x for x in projected if x["symbol"] == p["ticker"]), None)
        if found:
            found["shares"] += p["shares_to_buy"]
            found["total_value"] = round(found["shares"] * next((x["price_per_share"] for x in current_portfolio if x["symbol"] == p["ticker"]), 100), 2)
        else:
            projected.append({"symbol": p["ticker"], "shares": p["shares_to_buy"], "total_value": round(p["shares_to_buy"] * price, 2)})

    return {"investment_amount": monthly_amount, "strategy": strategy, "purchases": purchases, "projected_portfolio": projected}
