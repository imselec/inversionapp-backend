# portfolio_service.py

def load_portfolio():
    return {
        "UPS": 0.5577,
        "ABBV": 0.3574,
        "LMT": 0.1966
    }

def dividends_by_asset():
    return {
        "UPS": 12.4,
        "ABBV": 18.9,
        "LMT": 9.1
    }

def yield_history():
    return {
        "UPS": {"2023": 5.2, "2024": 6.1},
        "ABBV": {"2023": 4.3, "2024": 4.7},
        "LMT": {"2023": 3.1, "2024": 3.5}
    }

def recommendations():
    return [
        {"symbol": "UPS", "action": "buy"},
        {"symbol": "ABBV", "action": "hold"},
        {"symbol": "LMT", "action": "buy"}
    ]

def recommendation_candidates():
    return ["UPS", "ABBV", "LMT", "JNJ", "XOM", "CVX"]

def alerts():
    return [
        {"symbol": "UPS", "alert": "Price above 60"},
        {"symbol": "LMT", "alert": "Dividend increase"}
    ]

def history():
    return [
        {"date": "2026-01-01", "event": "Bought UPS"},
        {"date": "2026-01-15", "event": "Bought ABBV"}
    ]
