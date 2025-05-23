"""Testes do banco de dados."""

from sqlalchemy import select

from fast_api_curso.models import User


def test_create_user(session):
    """Criação de um user."""

    new_user = User(
        username='John Doe', email='john@doe.com', password='secret'
    )
    session.add(new_user)
    session.commit()
    user = session.scalar(
        select(User).where(User.username == 'John Doe'),
    )
    assert user.username == 'John Doe'
