import pytest
from src.paquete_proyecto.numbers import is_leap_year

@pytest.mark.parametrize("year, expected", [
    (2000, True),
    (1900, False),
    (2024, True),
    (2023, False),
])
def test_is_leap_year(year, expected):
    assert is_leap_year(year) == expected
