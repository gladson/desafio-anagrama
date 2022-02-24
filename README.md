# DESAFIO - ANAGRAMA

## INSTALACAO

### GIT CLONE

```
$ git clone https://github.com/gladson/desafio-anagrama.git desafio_anagrama
$ cd desafio_anagrama
```

### POETRY

[Poetry](https://python-poetry.org/docs/#installation)

> Caso queira instalar pelo poetry

```
$ poetry shell
Creating virtualenv desafio_anagrama in /desafio_anagrama/.venv
Virtual environment already activated: /desafio_anagrama/.venv

$ source .venv/bin/activate

$ poetry install
Installing dependencies from lock file

Package operations: 43 installs, 0 updates, 0 removals
  • ...
  • Installing mypy (0.931)
  • Installing pytest-cov (3.0.0)
  • Installing types-toml (0.10.4)

Installing the current project: desafio_anagrama (0.1.0)
```

### VENV - Python 3
> Caso nao queira o Poetry

```
$ python -m venv .venv
```
![image](https://user-images.githubusercontent.com/1013698/154902352-37db9dd6-7fbd-4ea9-a105-b38f42bd2178.png)
> Automaticamente o vscode vai pedir para selecionar a pasta para trabalho.

#### Para ativar e instalar o ambiente de desenvolvimento

```
$ .\.venv\Scripts\Activate.ps1
ou
$.\.venv\Scripts\Activate.bat
ou
$ source .\.venv\Scripts\activate

$ pip install -r requirements.txt 

Successfully installed asttokens-2.0.5 attrs-21.4.0 backcall-0.2.0 black-22.1.0 click-8.0.4 coverage-6.3.2 decorator-5.1.1 executing-0.8.2 flake8-4.0.1 iniconfig-1.1.1 ipdb-0.13.9 ipython-8.0.1 isort-5.10.1 jedi-0.18.1 matplotlib-inline-0.1.3 mccabe-0.6.1 mypy-0.931 mypy-extensions-0.4.3 packaging-21.3 parso-0.8.3 pathspec-0.9.0 pexpect-4.8.0 pickleshare-0.7.5 platformdirs-2.5.1 pluggy-1.0.0 prompt-toolkit-3.0.28 ptyprocess-0.7.0 pure-eval-0.2.2 py-1.11.0 pycodestyle-2.8.0 pyflakes-2.4.0 pygments-2.11.2 pyparsing-3.0.7 pytest-7.0.1 pytest-cov-3.0.0 six-1.16.0 stack-data-0.2.0 toml-0.10.2 tomli-2.0.1 traitlets-5.1.1 types-toml-0.10.4 typing-extensions-4.1.1 wcwidth-0.2.5
```
> Pronto ta lindao...

# RODAR PROJETO


## USANDO O MAKE

```
$ make run_desafio
python desafio_anagrama/main.py
6
```

## USANDO O PYTHON 

```
$ python desafio_anagrama/main.py 
6
```