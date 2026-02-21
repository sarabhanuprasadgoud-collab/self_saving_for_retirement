
from fastapi import Header, HTTPException, status
import os


#==========================================
# API key validation
#==========================================
def validate_api_key(x_api_key: str = Header( ... )):
    """
    Validates API key from request headers.
    Uses environment variable API_KEY for comparison.
    """
    expected_key = os.getenv("API_KEY")
    if not expected_key or x_api_key != expected_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")

#==========================================
# auth utilities
#==========================================