"""Aquivo principal."""

from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_api_curso.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    """Retorna uma mensagem em json."""
    return {'message': 'Olá mundo!'}


@app.get('/exercicio-html', response_class=HTMLResponse)
def exercicio_aula_02():
    """Retorna uma mensagem em html."""
    return """
    <html>
        <head>
            <title>Olá Mundo!</title>
        </head>
        <body>
            <h1>Olá Mundo!</h1>
        </body>
    </html>
    """
