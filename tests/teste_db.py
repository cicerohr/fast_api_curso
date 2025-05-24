"""Testes do banco de dados."""

from dataclasses import asdict

from sqlalchemy import select

from fast_api_curso.models import User


def test_create_user(session, mock_db_time):
    """Criação de um user."""
    with mock_db_time(model=User) as time:
        new_user = User(
            username='John Doe', email='john@doe.com', password='secret'
        )
        session.add(new_user)
        session.commit()
        user = session.scalar(select(User).where(User.username == 'John Doe'))
    assert asdict(user) == {
        'id': 1,
        'username': 'John Doe',
        'email': 'john@doe.com',
        'password': 'secret',
        'created_at': time,
        'updated_at': time,  # Exercício 02 aula 04
    }
