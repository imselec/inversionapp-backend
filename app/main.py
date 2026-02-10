from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers existentes y validados
from app.api.portfolio_snapshot import router as portfolio_snapshot_router
from app.api.portfolio_time_series import router as portfolio_time_series_router
from app.api.dividends_by_asset import router as dividends_router
from app.api.yield_history import router as yield_history_router
from app.api.recommendations import router as recommendations_router
from app.api.alerts import router as alerts_router
from app.api.history import router as history_router
from app.api.system import router as system_router

# Routers nuevos (ENDPOINTS QUE FALTABAN)
from app.api.recommendations_candidates import router as recommendations_candidates_router
from app.api.portfolio_actual import router as portfolio_actual_router
from app.api.investments_plan import router as investments_plan_router

app = FastAPI(
    title="InversionAPP Backend",
    version="1.0.0"
)

# CORS (Lovable + Render)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== Portfolio =====
app.include_router(
    portfolio_snapshot_router,
    prefix="/portfolio/snapshot",
    tags=["portfolio"]
)

app.include_router(
    portfolio_time_series_router,
    prefix="/portfolio/time-series",
    tags=["portfolio"]
)

app.include_router(
    dividends_router,
    prefix="/portfolio/dividends-by-asset",
    tags=["portfolio"]
)

app.include_router(
    yield_history_router,
    prefix="/portfolio/yield-history",
    tags=["portfolio"]
)

app.include_router(
    portfolio_actual_router,
    prefix="/portfolio",
    tags=["portfolio"]
)

# ===== Recommendations =====
app.include_router(
    recommendations_router,
    prefix="/recommendations",
    tags=["recommendations"]
)

app.include_router(
    recommendations_candidates_router,
    tags=["recommendations"]
)

# ===== Investments Plan =====
app.include_router(
    investments_plan_router,
    prefix="/investments",
    tags=["investments"]
)

# ===== System =====
app.include_router(
    alerts_router,
    prefix="/alerts",
    tags=["system"]
)

app.include_router(
    history_router,
    prefix="/history",
    tags=["system"]
)

app.include_router(
    system_router,
    prefix="/system",
    tags=["system"]
)
