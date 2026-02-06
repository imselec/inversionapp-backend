from app.models import MonthlyPlanRequest, MonthlyPlanResponse, RecommendedBuy, PostPurchaseSnapshot

def generate_monthly_plan(request: MonthlyPlanRequest = None) -> MonthlyPlanResponse:
    """
    Genera un plan de inversión mensual.
    Si se pasa un request, usa los parámetros; si no, usa valores por defecto.
    """
    # Valores por defecto
    monthly_amount = request.monthly_amount if request else 200

    # Ejemplo de recommended buys simuladas
    recommended_buys = [
        RecommendedBuy(symbol="PG", amount_usd=monthly_amount * 0.35, estimated_shares=0.41),
        RecommendedBuy(symbol="AVGO", amount_usd=monthly_amount * 0.33, estimated_shares=0.09),
        RecommendedBuy(symbol="JNJ", amount_usd=monthly_amount * 0.32, estimated_shares=0.38)
    ]

    # Simulación de snapshot post-compra
    snapshot = PostPurchaseSnapshot(
        total_value=12450,
        portfolio_yield=3.8,
        monthly_dividends_estimated=39.2
    )

    # Construir respuesta final
    response = MonthlyPlanResponse(
        monthly_amount=monthly_amount,
        recommended_buys=recommended_buys,
        post_purchase_snapshot=snapshot
    )

    return response
