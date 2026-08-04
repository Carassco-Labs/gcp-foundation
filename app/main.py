import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="GCP Foundation API",
    description="Production-ready FastAPI starter application for GCP Cloud Run",
    version="1.0.0",
)


class HealthResponse(BaseModel):
    status: str
    environment: str
    version: str


@app.get("/", tags=["General"])
def read_root():
    return {
        "message": "Welcome to GCP Foundation API",
        "docs": "/docs",
        "health": "/healthz",
    }


@app.get("/healthz", response_model=HealthResponse, tags=["Monitoring"])
def health_check():
    return HealthResponse(
        status="healthy",
        environment=os.getenv("APP_ENV", "development"),
        version="1.0.0",
    )
