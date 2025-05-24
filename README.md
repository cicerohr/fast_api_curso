# Estudo de Caso: FastApi com Poetry

Este tutorial tem o objetivo de configurar o ambiente de desenvolvimento para o 
FastApi utilizando o Pycharm, como editor de código, e o Poetry para gerenciamento 
de pacotes.

\* Obrigado [@dunossauro](https://dunossauro.com/)[^1] pelo excelente conteúdo! :smile:

> **ATENÇÃO**: este é um roteiro para instalação em uma máquina Windows visando 
> atender as minhas necessidades; portanto, não há qualquer garantia ou suporte 
> para este.

## O que ser&aacute; feito?

- [Instalar pyenv para Windows](#instalar-pyenv-para-windows2)
- [Instalar o pipx](#instalar-o-pipx3)
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

## Instalar pyenv para Windows[^2]

O pyenv é uma ferramenta que permite instalar e gerenciar várias versões do Python.

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

[Topo](#estudo-de-caso-fastapi-com-poetry)

---

## Instalar o pipx[^3]

O pipx é uma ferramenta que instala e executa aplicativos do Python em ambientes isolados.

1. Instale o pipx com o seguinte comando no PowerShell:
    ~~~PowerShell
    pip install --upgrade pipx
    ~~~
   
   - Verifique se o pipx foi instalado corretamente com o seguinte comando no PowerShell:
       ~~~PowerShell
       pipx --version
       ~~~
   
   - Adicione o pipx ao PATH com o seguinte comando no PowerShell:
       ~~~PowerShell
       pipx ensurepath
       ~~~
   
   - Verifique se o pipx foi adicionado ao PATH com o seguinte comando no PowerShell:
       ~~~PowerShell
       where pipx
       ~~~
   
2. Instale o Poetry[^4] com o seguinte comando no PowerShell:
    O Poetry é um gerenciador de pacotes Python e seu ambiente virtual.
    ~~~PowerShell
    pipx install poetry
    ~~~
   
   - Verifique se o Poetry foi instalado corretamente com o seguinte comando no PowerShell:
       ~~~PowerShell
       poetry --version
       ~~~
   
3. Instale o ignr[^5] com o seguinte comando no PowerShell:
   O ignr é um gerenciador de modelos de arquivos [gitignore](https://git-scm.com/docs/gitignore)[^6]. 
   ~~~PowerShell
    pipx install ignr
    ~~~
   
   - Lista todos os modelos .gitignore disponíveis no gitignore.io.
       ~~~PowerShell
       ignr -l
       ~~~

[Topo](#estudo-de-caso-fastapi-com-poetry)

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

[Topo](#estudo-de-caso-fastapi-com-poetry)

---

## Abrir o projeto no PyCharm

Abra o projeto no PyCharm como um projeto existente.

[Topo](#estudo-de-caso-fastapi-com-poetry)

---

## Configurar o Poetry

Crie o ambiente virtual com o seguinte comando no PowerShell:
~~~PowerShell
poetry install
~~~~

[Topo](#estudo-de-caso-fastapi-com-poetry)

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
- Usando o FastApi na rede local

    Este comando irá executar o servidor do FastApi na rede local podendo ser acessado por outros dispositivos da rede.
    ~~~PowerShell
    fastapi dev src/fast_api_curso/app.py --host 0.0.0.0
    ~~~

    Acesse o seguinte endereço para acessar o servidor do FastApi na rede local:
    ~~~html
    http://<ip-address>:8000/
    ~~~

[Topo](#estudo-de-caso-fastapi-com-poetry)

---

## Ferramentas de desenvolvimento

### Instalar Ruff

A ferramenta Ruff é um analisador estático (linter) e formatador de código Python.

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

O PyTest é um framework de testes unitários para Python e o PyTest-Cov é um analisador de cobertura de testes.

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

A ferramenta Taskipy é um gerenciador de tarefas para Python.

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
- Para listar as tarefas, execute o comando `task --list` no terminal.

[Topo](#estudo-de-caso-fastapi-com-poetry)

---

## Referências:

[^1]: MENDES, E. **FastAPI do Zero**. Disponível em:<https://fastapidozero.dunossauro.com/estavel/>.\*

[^2]: KOTARI, K. K. **pyenv for Windows**. Disponível em:<https://github.com/pyenv-win/pyenv-win?tab=readme-ov-file#introduction>.

[^3]: SMITH, C. **pipx — Install and Run Python Applications in Isolated Environments**. Disponível em: <https://pipx.pypa.io/stable/installation/>.

[^4]: POETRY COMMUNITY. **Poetry: Python packaging and dependency management made easy**. Disponível em: <https://python-poetry.org/docs/>.

[^5]: YADAV, A; WARD, A. **ignr.py**. Disponível em:<https://github.com/Antrikshy/ignr.py?tab=readme-ov-file#ignrpy>.

[^6]: GIT COMMUNITY. **Git - gitignore Documentation**. Disponível em: <https://git-scm.com/docs/gitignore/pt_BR>.
