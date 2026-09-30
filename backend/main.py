from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.config import (
    ALLOWED_ORIGINS,
    GEMINI_MODEL,
    MOCK_MODE,
)

from backend.routes import router


# --------------------------------
# CREATE FASTAPI APPLICATION
# --------------------------------

app = FastAPI(
    title="LegalEase API",
    description="AI-Powered Legal Document Generator",
    version="1.0.0",
)


# --------------------------------
# CORS CONFIGURATION
# --------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------
# INCLUDE API ROUTES
# --------------------------------

app…