from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel, field_validator
from typing import Dict, Optional
import json
import os

router = APIRouter()

CONFIG_FILE = "config.json"
API_KEY = os.getenv("CONFIG_API_KEY", "supersecretkey")  # Cambiar en producción


# ==========================
# 📦 MODELO
# ==========================

class BenchmarkUpdate(BaseModel):
    benchmark: Dict[str, float]

    @field_validator("benchmark")
    @classmethod
    def validate_benchmark(cls, v):
        if not v:
            raise ValueError("Benchmark cannot be empty")

        total = sum(v.values())

        if abs(total - 100) > 0.01:
            raise ValueError(f"Benchmark must sum to 100%. Current sum: {total}")

        for sector, weight in v.items():
            if weight < 0:
                raise ValueError(f"Sector {sector} has negative weight")

        return v


# ==========================
# 🔐 AUTH VALIDATION
# ==========================

def validate_api_key(x_api_key: Optional[str]):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")


# ==========================
# 📂 UTILS
# ==========================

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_config(config_data: dict):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config_data, f, indent=4)


# ==========================
# 🚀 ENDPOINT
# ==========================

@router.post("/benchmark")
def update_benchmark(
    payload: BenchmarkUpdate,
    x_api_key: Optional[str] = Header(None)
):
    validate_api_key(x_api_key)

    config = load_config()
    config["benchmark"] = payload.benchmark
    save_config(config)

    return {
        "status": "success",
        "message": "Benchmark updated successfully",
        "benchmark": payload.benchmark
    }
