"""Aquivo principal."""

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    """Retorna uma mensagem."""
    return {'message': 'Olá mundo!'}
