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


def test_create_user(client):
    """Retorna um usuário com id."""
    # client = TestClient(app)
    response = client.post(
        '/users/',
        json={
            'username': 'John',
            'email': 'iE2hT@example.com',
            'password': '123456',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'John',
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
                'username': 'John',
                'email': 'iE2hT@example.com',
            },
        ]
    }


def test_update_user(client):
    """Altera um user no json."""
    response = client.put(
        '/users/1',
        json={
            'username': 'John Doe',
            'email': 'john@doe.com',
            'password': '123456',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'John Doe',
        'email': 'john@doe.com',
    }


def test_update_user_not_found(client):
    """Verifica se o user nao foi encontrado."""
    response = client.put(
        '/users/2',
        json={
            'username': 'Jane Doe',
            'email': 'Jane@doe.com',
            'password': '654321',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    """Deleta um user do json."""
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'John Doe',
        'email': 'john@doe.com',
    }


def test_delete_user_not_found(client):
    """Verifica se o user nao foi encontrado."""
    response = client.delete('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found!'}


def test_exercicio_ola_mundo_em_html(client):
    """Retorna uma mensagem em html."""
    # client = TestClient(app)
    response = client.get('/exercicio-html')
    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá Mundo!</h1>' in response.text
