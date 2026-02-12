import yfinance as yf
import pandas as pd
import socket
from functools import lru_cache


socket.setdefaulttimeout(5)  # 🔒 timeout global


@lru_cache(maxsize=32)
def get_market_data(ticker: str):

    try:
        data = yf.Ticker(ticker)

        hist = data.history(period="1mo")

        if hist.empty:
            return None

        price = hist["Close"].iloc[-1]
        returns = hist["Close"].pct_change().dropna()

        momentum_30 = (
            (hist["Close"].iloc[-1] / hist["Close"].iloc[0]) - 1
            if len(hist) > 5 else 0
        )

        volatility = returns.std() if not returns.empty else 0

        max_price = hist["Close"].max()
        drawdown = (max_price - price) / max_price if max_price > 0 else 0

        info = data.info
        dividend_yield = info.get("dividendYield", 0) or 0

        return {
            "price": float(price),
            "momentum_30": float(momentum_30),
            "volatility": float(volatility),
            "drawdown": float(drawdown),
            "dividend_yield": float(dividend_yield),
        }

    except Exception:
        # 🔒 Si Yahoo falla, no bloquea el sistema
        return None
