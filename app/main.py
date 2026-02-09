from fastapi import FastAPI

from app.api.system import router as system_router
from app.api.portfolio import router as portfolio_router
from app.api.investments import router as investments_router

app = FastAPI(title="InversionAPP Backend")

app.include_router(system_router)
app.include_router(portfolio_router)
app.include_router(investments_router)
