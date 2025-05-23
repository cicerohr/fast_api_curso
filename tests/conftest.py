"""Configuração de fixtures para os testes."""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_api_curso.app import app
from fast_api_curso.models import table_register


@pytest.fixture
def client():
    """Bloco de teste reutilizável do TestClient."""
    return TestClient(app)


@pytest.fixture
def session():
    """Bloco de teste reutilizável da sessão do banco de dados."""
    engine = create_engine('sqlite:///:memory:')
    table_register.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    table_register.metadata.drop_all(engine)
