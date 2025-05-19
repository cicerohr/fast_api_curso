"""Schemas para validação dos dados."""
from pydantic import BaseModel

class Message(BaseModel):
    """Mensagem."""
    message: str
