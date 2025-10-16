import pytest
from src.numbers import safe_divide

def test_safe_divide_ok():
    assert safe_divide(10, 2) == 5

def test_safe_divide_zero():
    with pytest.raises(ValueError, match="division by zero"):
        safe_divide(10, 0)

def test_safe_divide_type_error():
    with pytest.raises(TypeError):
        safe_divide("3", 2)
