from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers
from app.api.recommendations import router as recommendations_router
from app.api.config import router as config_router

app = FastAPI(
    title="InversionAPP Backend",
    version="3.0.0"
)

# ==============================
# CORS (Lovable / Render ready)
# ==============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# Routers
# ==============================
app.include_router(
    recommendations_router,
    prefix="/recommendations",
    tags=["recommendations"]
)

app.include_router(
    config_router,
    prefix="/config",
    tags=["config"]
)

# ==============================
# Health Endpoints
# ==============================
@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "InversionAPP Backend",
        "version": "3.0.0"
    }


@app.get("/system/status")
def system_status():
    return {
        "status": "running"
    }
