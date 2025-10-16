import pytest
from src.numbers import unique_sorted


def test_unique_sorted():
    seq = [3, 1, 2, 3, 2] 
    esperado = [1, 2, 3]
    assert unique_sorted(seq) == esperado

def test_unique_sorted_cadenas():
    seq = ["b", "a", "b"]
    esperado = ["a", "b"]
    assert unique_sorted(seq) == esperado