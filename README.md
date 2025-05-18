# FastApi do Zero
Ref.: [FastAPI do ZERO](https://fastapidozero.dunossauro.com/estavel/) 
(Obrigado [@dunossauro](https://dunossauro.com/) pelo excelente conteúdo! :smile:)

> **ATENÇÃO**: este é um roteiro para instalação em uma máquina Windows para 
atender as minhas necessidades; portanto, não há qualquer garantia ou suporte 
para este.

## O que será feito?

- Instalar o [pyenv](https://github.com/pyenv-win/pyenv-win) para Windows;
- Instalar o pipx;
- Instalar uma versão Python;
- Instalar o [Poetry](https://python-poetry.org/);
- Criar um projeto FastApi com o Poetry;
- Abrir o projeto no PyCharm;
- Configurar o [Poetry](https://python-poetry.org/);
- Configurar o [pipx](https://github.com/pypa/pipx);
- Configurar o [FastApi](https://fastapi.tiangolo.com/);
- Configurar o [PyCharm](https://www.jetbrains.com/pycharm/);
- Ferramentas de desenvolvimento;
  - Instalar [ignr](https://github.com/Antrikshy/ignr.py?tab=readme-ov-file) (Ignorador de arquivos);
  - instalar [Ruff](https://beta.ruff.rs/) (Analisador estático e formatador de código);
  - Instalar [PyTest](https://docs.pytest.org/en/latest/) (Testes unitários);
  - Instalar [pytest-cov](https://pypi.org/project/pytest-cov/) (Cobertura de testes);
  - Instalar Taskipy (_Script_ para execução de tarefas);

### Instalar pyenv para Windows

#### Instalar pyenv pelo PowerShell
Ref.: [pyenv para Windows (GitHub)](https://github.com/pyenv-win/pyenv-win?tab=readme-ov-file#introduction)

1. Instale o pyenv-win com o seguinte comando:
    ~~~PowerShell
    Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
    ~~~
   
2. Reiniciar o PowerShell.
3. Verifique se o pyenv foi instalado corretamente com o seguinte comando:
    ~~~PowerShell
    pyenv --version
    ~~~
   
4. Verifique a lista de versões Python suportadas pelo pyenv-win com o seguinte comando:
    ~~~PowerShell
    pyenv install -l
    ~~~
   
5. Instale uma versão Python com o seguinte comando:
    ~~~PowerShell
    pyenv install <version>
    ~~~
   
6. Defina a versão Python global com o seguinte comando:
    ~~~PowerShell
    pyenv global <version>
    ~~~

7. Verifique qual versão Python você está usando e seu caminho com o seguinte comando:
    ~~~PowerShell
    pyenv version
    ~~~

8. Verifique se o Python está funcionando com o seguinte comando:
    ~~~PowerShell
    python -c "import sys; print(sys.executable)"
    ~~~
