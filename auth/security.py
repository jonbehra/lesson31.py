from fastapi import FastAPI, Depends, HTTPExpection, status
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEYS")
API_KEY_NAME = "api-key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPExpection(
            status_code =status.HTTP_401_UNATHORIZED,
            detailed="Invalid API Key",
        )
    return api_key