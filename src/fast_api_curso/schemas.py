"""Schemas para validação dos dados."""

from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    """Validador de mensagem."""

    message: str


class UserSchema(BaseModel):
    """Validador de usuário."""

    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    """Validador de usuário sem mostrar a senha."""

    id: int
    username: str
    email: EmailStr


class UserDB(UserSchema):
    """Validador de usuário com id."""

    id: int


class UserList(BaseModel):
    """Validador da lista de usuários."""

    users: list[UserPublic]
