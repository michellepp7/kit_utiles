import pytest
from src.numbers import sum_list

def test_sum_list():
    nums = [1, 2, 3, 4]
    esperado = 10
    assert sum_list(nums) == esperado

def test_sum_list_vacia():
    nums = []
    esperado = 0
    assert sum_list(nums) == esperado
