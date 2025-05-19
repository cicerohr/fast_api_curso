"""Aquivo principal."""
from http import HTTPStatus
from fastapi import FastAPI
from fast_api_curso.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    """Retorna uma mensagem em json."""
    return {'message': 'Olá mundo!'}
