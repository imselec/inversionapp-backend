import os
from fastapi import Header, HTTPException

def verify_api_key(x_api_key: str = Header(None)):

    expected_key = os.getenv("CONFIG_API_KEY")

    if not expected_key:
        raise HTTPException(
            status_code=500,
            detail="API key not configured on server"
        )

    if x_api_key != expected_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )
