"""
FastAPI application entry point.
"""

from fastapi import FastAPI

from src.config import settings

app = FastAPI(
    title="Shopifake Chatbot",
    description="Shopifake chatbot service",
    version="1.0.0",
)


@app.get("/")
async def read_root():
    """
    Hello World endpoint.

    Returns:
        dict: A simple greeting message
    """
    return {"message": "Hello World"}


@app.get("/health")
async def health_check():
    """
    Health check endpoint.

    Returns:
        dict: Service health status
    """
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT,
    }
