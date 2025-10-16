import pytest
from src.strings import word_count


@pytest.fixture
def texto():
    return "Hola, hola... ¿Qué tal? Tal vez bien: hola!"


def test_word_count(texto):
    resultado = word_count(texto)
    assert resultado["hola"] == 3
    assert resultado["tal"] == 2
    assert resultado["que"] == 1
    assert "inexistente" not in resultado
