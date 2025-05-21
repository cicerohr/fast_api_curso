"""Aquivo principal."""

from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fast_api_curso.schemas import (
    Message,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()
database = []  # Lista provisória para fins de estudo


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    """Retorna uma mensagem em json."""
    return {'message': 'Olá mundo!'}


@app.post(
    '/users/',
    status_code=HTTPStatus.CREATED,
    response_model=UserPublic,
)
def create_user(user: UserSchema):
    """Cria um novo user e retorna o mesmo em json."""
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    """Retorna uma lista de users em json."""
    return {'users': database}


@app.put(
    '/users/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=UserPublic,
)
def update_user(user_id: int, user: UserSchema):
    """Altera um user no json."""
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found!',
        )
    database[user_id - 1] = user_with_id
    return user_with_id


@app.delete(
    '/users/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=UserPublic,
)
def delete_user(user_id: int):
    """Deleta um user do json."""
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found!',
        )
    return database.pop(user_id - 1)


@app.get('/exercicio-html', response_class=HTMLResponse)
def exercicio_aula_02():
    """Exercício 02 - Retorna uma mensagem em html."""
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
