"""A estrutura de um teste, costuma contar com 3 ou 4 fases importantes.

- Organizar (arrange)
- Executar (act)
- Afirmar (assert)
- teardown (cleanup)
"""

from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api_curso.app import app


def test_read_root_retornar_ok_e_ola_mundo():
    """Retorna uma mensagem json.

    (Arrange, Act, Assert)
    - Arrange (Arranjo);
    - Act (Ação);
    - Assert (Afirmar).
    """
    client = TestClient(app)  # Arrange (Organização)
    response = client.get('/')  # Act (Ação)
    assert response.status_code == HTTPStatus.OK  # Assert (Afirmar)
    assert response.json() == {'message': 'Olá mundo!'}  # Assert (Afirmar)


def test_exercicio_ola_mundo_em_html():
    """Retorna uma mensagem em html."""
    client = TestClient(app)
    response = client.get('/exercicio-html')
    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá Mundo!</h1>' in response.text
