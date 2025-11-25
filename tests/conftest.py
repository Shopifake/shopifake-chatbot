"""
Pytest configuration and fixtures.
"""

import pytest
from httpx import ASGITransport, AsyncClient

from src.main import app


@pytest.fixture(scope="function")
async def client():
    """
    Create an async test client.
    """
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as test_client:
        yield test_client
