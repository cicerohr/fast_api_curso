"""Modelos das tabelas para o banco de dados."""

from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_register = registry()  # registro das tabelas


@table_register.mapped_as_dataclass
class User:
    """Cria a tabela 'users'.

    Os atributos da classe representam as colunas da tabela 'users'.
    Os atributos são mapeados para as colunas da tabela usando o SQLAlchemy e
    implementam as características de cada registro da tabela com
    mapped_column.

    Attributes:
        id (int): ID do usuário.
        username (str): Nome do usuário.
        email (str): Email do usuário.
        password (str): Senha do usuário.
        created_at (datetime): Data de criação do usuário.

    Returns:
        None
    """

    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False,
        server_default=func.now(),
    )
