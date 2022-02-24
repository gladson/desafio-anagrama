import pathlib

import pytest
import toml


from desafio_anagrama.main import LIST_WORDS_A, LIST_WORDS_B


@pytest.fixture
def version():
    BASE_PATH = pathlib.Path().absolute()
    file_pyproject = BASE_PATH / "pyproject.toml"
    with open(file_pyproject) as open_file_pyproject:
        dict_file_project = toml.load(open_file_pyproject)
        return dict_file_project["tool"]["poetry"]["version"]


@pytest.fixture
def list_words_a_success():
    return LIST_WORDS_A


@pytest.fixture
def list_words_b_success():
    return LIST_WORDS_B


@pytest.fixture
def list_words_b_error():
    LIST_WORDS_B_ERROR = LIST_WORDS_B.copy()
    LIST_WORDS_B_ERROR.remove("umido")
    return LIST_WORDS_B_ERROR


# if __name__ == "__main__":
#     version()
