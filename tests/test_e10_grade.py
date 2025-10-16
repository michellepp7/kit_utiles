import pytest
from src.paquete_proyecto.numbers import grade

@pytest.mark.parametrize("score, expected", [
    (100, "A"),
    (90, "A"),
    (89, "B"),
    (80, "B"),
    (79, "C"),
    (70, "C"),
    (69, "D"),
    (60, "D"),
    (59, "F"),
    (0, "F")
])

def test_grade_limites(score, expected):
    assert grade(score) == expected

@pytest.mark.parametrize("score", [-1, 101])

def test_grade_fuera_de_rango(score):
    with pytest.raises(ValueError):
        grade(score)

def test_grade_no_entero():
    with pytest.raises(TypeError):
        grade(85.0)
