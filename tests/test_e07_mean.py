import pytest
from src.paquete_proyecto.numbers import mean

def test_mean_normal():
    assert mean([1, 2, 3, 4]) == 2.5


def test_mean_empty():
    with pytest.raises(ValueError, match="empty sequence"):
        mean([])
