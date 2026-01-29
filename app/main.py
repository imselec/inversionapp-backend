from fastapi import FastAPI

# Routers
from app.routes import portfolio
from app.routes import recommendations
from app.routes import recommendation_candidates
from app.routes import system

# Crear la app ANTES de usarla
app = FastAPI(
    title="InversionAPP Backend",
    version="1.0.0"
)

# Registrar routers
app.include_router(portfolio.router)
app.include_router(recommendations.router)
app.include_router(recommendation_candidates.router)
app.include_router(system.router)


# Endpoint raíz (opcional pero recomendado)
@app.get("/")
def root():
    return {
        "app": "InversionAPP Backend",
        "status": "running"
    }
