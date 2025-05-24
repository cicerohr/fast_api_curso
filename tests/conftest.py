"""Configuração de fixtures para blocos reutilizáveis nos testes."""

from contextlib import contextmanager
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
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


@contextmanager
def _mock_db_time(*, model, time=datetime(2025, 5, 20)):
    """Mock para o evento pre_commit.

    Args:
        model (object): Objeto model.
        time (datetime): Data para o teste de criação do usuário.

    Returns:
        None
    """

    def fake_time_hook(mapper, connection, target):
        """Mock para o evento pre_commit.
        Inserindo data de criação no banco de dados para poder validar os
        testes.

        Args:
            mapper (object): Objeto mapper.
            connection (object): Objeto connection.
            target (object): Objeto target.

        Returns:
            None
        """
        if hasattr(target, 'created_at'):
            target.created_at = time

    event.listen(
        model,
        'before_insert',
        fake_time_hook,
    )
    yield time
    event.remove(
        model,
        'before_insert',
        fake_time_hook,
    )


@pytest.fixture
def mock_db_time():
    """Mock para o evento pre_commit."""
    return _mock_db_time
