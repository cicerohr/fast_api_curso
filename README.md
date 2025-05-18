# Estudo de Caso: FastApi com Poetry

Este tutorial tem o objetivo de configurar o ambiente de desenvolvimento para o 
FastApi utilizando o Pycharm, como editor de código, e o Poetry para gerenciamento 
de pacotes.

> **ATENÇÃO**: este é um roteiro para instalação em uma máquina Windows visando 
> atender as minhas necessidades; portanto, não há qualquer garantia ou suporte 
> para este.

- [O que ser&aacute; feito?](#o-que-ser&aacute;-feito?)
- [Instalar pyenv para Windows](#instalar-pyenv-para-windows)
- [Instalar o pipx](#instalar-o-pipx)
- [Criar um projeto FastApi com o Poetry](#criar-um-projeto-fastapi-com-o-poetry)
- [Abrir o projeto no PyCharm](#abrir-o-projeto-no-pycharm)
- [Configurar o Poetry](#configurar-o-poetry)
- [Instalar o FastApi](#instalar-o-fastapi)
- [Ferramentas de desenvolvimento](#ferramentas-de-desenvolvimento)
  - [Instalar Ruff](#instalar-ruff)
  - [Instalar PyTest e PyTest-Cov](#instalar-pytest-e-pytest-cov)
  - [Instalar Taskipy](#instalar-taskipy)
- [Referências](#referências)

---

## O que ser&aacute; feito?

- Instalar o [pyenv](https://github.com/pyenv-win/pyenv-win) para Windows (Ferramenta que permite instalar e gerenciar várias versões do Python);
  - Instalar uma versão Python;
- Instalar o [pipx](https://github.com/pypa/pipx?tab=readme-ov-file#on-windows) (Instala e executa aplicativos Python em ambientes isolados);
  - Instalar o [Poetry](https://python-poetry.org/) (Gerenciador de pacotes Python e seu ambiente virtual);
  - Instalar o [ignr](https://github.com/Antrikshy/ignr.py?tab=readme-ov-file) (Ignorador de arquivos);
- Criar um projeto FastApi com o Poetry;
- Abrir o projeto no PyCharm;
- Configurar o [Poetry](https://python-poetry.org/);
- Instalar o [FastApi](https://fastapi.tiangolo.com/);
  - Executar o FastApi;
- Ferramentas de desenvolvimento;
  - instalar [Ruff](https://docs.astral.sh/ruff/installation/) (Analisador estático e formatador de código);
  - Instalar [PyTest](https://docs.pytest.org/en/latest/) (Testes unitários);
  - Instalar [pytest-cov](https://pypi.org/project/pytest-cov/) (Cobertura de testes);
  - Instalar [Taskipy](https://github.com/taskipy/taskipy?tab=readme-ov-file) (_Script_ para execução de tarefas);

---

## Instalar pyenv para Windows

### Instalar pyenv pelo PowerShell

1. Instale o pyenv-win com o seguinte comando no PowerShell:
    ~~~PowerShell
    Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
    ~~~
   
2. Reiniciar o PowerShell.
3. Verifique se o pyenv foi instalado corretamente com o seguinte comando no PowerShell:
    ~~~PowerShell
    pyenv --version
    ~~~
   
4. Verifique a lista de versões Python suportadas pelo pyenv-win com o seguinte comando no PowerShell:
    ~~~PowerShell
    pyenv install -l
    ~~~
   
5. Instale uma versão Python com o seguinte comando no PowerShell:
    ~~~PowerShell
    pyenv install <version>
    ~~~
   
6. Defina a versão Python global com o seguinte comando no PowerShell:
    ~~~PowerShell
    pyenv global <version>
    ~~~

7. Verifique qual versão Python você está usando e seu caminho com o seguinte comando no PowerShell:
    ~~~PowerShell
    pyenv version
    ~~~

8. Verifique se o Python está funcionando com o seguinte comando no PowerShell:
    ~~~PowerShell
    python -c "import sys; print(sys.executable)"
    ~~~
\* Suporte para o erro [**UnauthorizedAccess**](https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#powershell) no Windows.

---

## Instalar o pipx

1. Instale o pipx com o seguinte comando no PowerShell:
    ~~~PowerShell
    pip install --upgrade pipx
    ~~~
   
2. Verifique se o pipx foi instalado corretamente com o seguinte comando no PowerShell:
    ~~~PowerShell
    pipx --version
    ~~~
   
3. Adicione o pipx ao PATH com o seguinte comando no PowerShell:
    ~~~PowerShell
    pipx ensurepath
    ~~~
   
   1. Verifique se o pipx foi adicionado ao PATH com o seguinte comando no PowerShell:
       ~~~PowerShell
       where pipx
       ~~~
   
   2. Instale o Poetry com o seguinte comando no PowerShell:
       ~~~PowerShell
       pipx install poetry
       ~~~
   
4. Verifique se o Poetry foi instalado corretamente com o seguinte comando no PowerShell:
    ~~~PowerShell
    poetry --version
    ~~~
   
5. Instale o ignr com o seguinte comando no PowerShell:
    ~~~PowerShell
    pipx install ignr
    ~~~
   
6. Lista todos os modelos .gitignore disponíveis no gitignore.io.
    ~~~PowerShell
    ignr -l
    ~~~

---

## Criar um projeto FastApi com o Poetry

1. Criar um projeto com o seguinte comando no PowerShell:
    ~~~PowerShell
    poetry new <project-name>
    ~~~ 
   Acesse o diretório do projeto com o seguinte comando no PowerShell:
    ~~~PowerShell
    cd <project-name>
    ~~~
   Isso criará o diretório de project-name com o seguinte conteúdo:
    ~~~PowerShell
    project-name
    ├── pyproject.toml
    ├── README.md
    ├── src
    │   └── project_name
    │       └── __init__.py
    └── tests
        └── __init__.py
    ~~~~
2. Para usar a versão do Python específica, execute o seguinte comando dentro do diretório do projeto:
    ~~~PowerShell
    pyenv local <version>
    ~~~
---

## Abrir o projeto no PyCharm

Abra o projeto no PyCharm como um projeto existente.

---

## Configurar o Poetry

Crie o ambiente virtual com o seguinte comando no PowerShell:
~~~PowerShell
poetry install
~~~~

---

## Instalar o FastApi

Instale o FastApi com o seguinte comando no PowerShell:
~~~PowerShell
poetry add fastapi
~~~

Executar o servidor do FastApi
~~~PowerShell
fastapi dev src/fast_api_curso/app.py
~~~
- Endereço do servidor [http://127.0.0.1:8000]( http://127.0.0.1:8000)
- Documentação automática interativa do FastApi
  - [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
  - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
 
---

## Ferramentas de desenvolvimento

### Instalar Ruff

Instale o Ruff com o seguinte comando no terminal:
~~~PowerShell
poetry add --group dev ruff
~~~

Altere o arquivo `pyproject.toml` adicionando a seguinte configuração:
~~~toml
[tool.ruff]
line-length = 79
extend-exclude = ["migrations"]

[tool.ruff.lint]
preview = true
select = ["D", "E", "F", "I", "N", "PL", "PT", "W"]

[tool.ruff.format]
preview = true
quote-style = "single"
~~~

### Instalar PyTest e PyTest-Cov

Instale o PyTest e PyTest-Cov com o seguinte comando no terminal:
~~~PowerShell
poetry add --group dev pytest pytest-cov
~~~

Altere o arquivo `pyproject.toml` adicionando a seguinte configuração:
~~~toml
[tool.pytest.ini_options]
pythonpath = ["."]
addopts = "-p no:warnings"
~~~

### Instalar Taskipy

Instale o Taskipy com o seguinte comando no terminal:
~~~PowerShell
poetry add --group dev taskipy
~~~

#### Configurar as tarefas

Configure o Taskipy editando o arquivo `pyproject.toml`:

~~~toml
[tool.taskipy.tasks]
lint = "ruff check . && ruff check . --diff"
format = "ruff check . --fix && ruff format ."
run = "fastapi dev src/fast_api_curso/app.py"
pre_test = "task lint"
test = "pytest -s -x --cov=src/fast_api_curso -vv"
post_test = "coverage html"
~~~

#### Executar as tarefas

- Para rodar o servidor, execute o comando `task run` no terminal;
- Para rodar o lint, execute o comando `task lint` no terminal;
- Para formatar o código, execute o comando `task format` no terminal;
- Para rodar o lint, execute o comando `task pre_test` no terminal;
- Para rodar os testes, execute o comando `task test` no terminal;
- Para ver o relatório de cobertura, execute o comando `task post_test` no terminal.
    - Escreve o relatório HTML em [http://localhost:63342/fast_api_curso/htmlcov/index.html](http://localhost:63342/fast_api_curso/htmlcov/index.html)

---

## Referências:

MENDES, E. **FastAPI do Zero**. Disponível em:<https://fastapidozero.dunossauro.com/estavel/>.\*

KOTARI, K. K. **pyenv for Windows**. Disponível em:<https://github.com/pyenv-win/pyenv-win?tab=readme-ov-file#introduction>.

SMITH, C. **pipx — Install and Run Python Applications in Isolated Environments**. Disponível em: <https://pipx.pypa.io/stable/installation/>.

POETRY COMMUNITY. **Poetry: Python packaging and dependency management made easy**. Disponível em: <https://python-poetry.org/docs/>.

YADAV, A; WARD, A. **ignr.py**. Disponível em:<https://github.com/Antrikshy/ignr.py?tab=readme-ov-file#ignrpy>. 

\* Obrigado [@dunossauro](https://dunossauro.com/) pelo excelente conteúdo! :smile:

---
