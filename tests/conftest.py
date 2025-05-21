import pytest
from fastapi.testclient import TestClient

from fast_api_curso.app import app


@pytest.fixture
def client():
    """Bloco de teste reutilizável do TestClient."""
    return TestClient(app)
