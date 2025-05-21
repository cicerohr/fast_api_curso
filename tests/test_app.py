"""A estrutura de um teste, costuma contar com 3 ou 4 fases importantes.

- Organizar (arrange)
- Executar (act)
- Afirmar (assert)
- teardown (cleanup)
"""

from http import HTTPStatus


def test_read_root_retornar_ok_e_ola_mundo(client):
    """Retorna uma mensagem json.

    (Arrange, Act, Assert)
    - Arrange (Arranjo);
    - Act (Ação);
    - Assert (Afirmar).
    """
    # client = TestClient(app)  # Arrange (Organização)
    response = client.get('/')  # Act (Ação)
    assert response.status_code == HTTPStatus.OK  # Assert (Afirmar)
    assert response.json() == {'message': 'Olá mundo!'}  # Assert (Afirmar)


def test_crate_user(client):
    """Retorna um usuário com id."""
    # client = TestClient(app)
    response = client.post(
        '/users/',
        json={
            'username': 'test',
            'email': 'iE2hT@example.com',
            'password': '123456',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'test',
        'email': 'iE2hT@example.com',
    }


def test_read_users(client):
    """Lista todos os users."""
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'test',
                'email': 'iE2hT@example.com',
            },
        ]
    }


def test_exercicio_ola_mundo_em_html(client):
    """Retorna uma mensagem em html."""
    # client = TestClient(app)
    response = client.get('/exercicio-html')
    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá Mundo!</h1>' in response.text
