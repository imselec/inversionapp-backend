# test_endpoints.py
import requests

BASE_URL = "http://127.0.0.1:8000"

ENDPOINTS = [
    "/portfolio/snapshot",
    "/portfolio/time-series",
    "/portfolio/dividends-by-asset",
    "/portfolio/yield-history",
    "/portfolio",
    "/recommendations/monthly",
    "/recommendations/candidates",
    "/investments/plan",
    "/alerts",
    "/history",
    "/system/status"
]

def test_endpoints():
    print("=== Testing InversionAPP Backend ===\n")
    for ep in ENDPOINTS:
        url = BASE_URL + ep
        try:
            resp = requests.get(url, timeout=5)
            if resp.status_code == 200:
                print(f"[OK] {url} -> Status 200")
            else:
                print(f"[FAIL] {url} -> Status {resp.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[FAIL] {url} -> {e}")

if __name__ == "__main__":
    test_endpoints()
