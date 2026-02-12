from pathlib import Path
import json
from typing import Dict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_FILE = BASE_DIR / "config.json"

DEFAULT_CONFIG = {
    "monthly_investment": 200,
    "benchmark": {
        "Technology": 28.0,
        "Healthcare": 13.0,
        "Financials": 12.5,
        "Consumer Defensive": 6.5,
        "Energy": 4.5,
        "REIT": 2.5
    }
}


def load_config() -> Dict:
    if not CONFIG_FILE.exists():
        return DEFAULT_CONFIG

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return DEFAULT_CONFIG


def save_config(config: Dict):
    """
    Guarda configuración en config.json
    """
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)
