"""Schemas para validação dos dados."""

from pydantic import BaseModel


class Message(BaseModel):
    """Validador de mensagem."""

    message: str
