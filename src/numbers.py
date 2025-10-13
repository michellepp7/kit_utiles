"""
Módulo numbers.py
Funciones de utilidades numéricas para practicar pruebas unitarias.
"""

from typing import Iterable, Union

Number = Union[int, float]


def sum_list(nums: Iterable[Number]) -> Number:
    """
    Devuelve la suma de los elementos de una lista.
    Si la lista está vacía, devuelve 0.
    """
    return sum(nums) if nums else 0


def unique_sorted(seq: Iterable[Number]) -> list[Number]:
    """
    Elimina duplicados y devuelve una lista ordenada ascendente.
    """
    return sorted(set(seq))


def is_leap_year(year: int) -> bool:
    """
    Determina si un año es bisiesto según el calendario gregoriano.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def safe_divide(a: Number, b: Number) -> float:
    """
    Realiza una división segura:
    - Lanza ValueError si b == 0.
    - Lanza TypeError si los argumentos no son numéricos.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numbers")
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def mean(nums: Iterable[Number]) -> float:
    """
    Calcula la media aritmética.
    Lanza ValueError si la lista está vacía.
    """
    nums = list(nums)
    if not nums:
        raise ValueError("empty sequence")
    return sum(nums) / len(nums)


def grade(score: int) -> str:
    """
    Devuelve la calificación literal según la puntuación numérica:
      A: 90-100
      B: 80-89
      C: 70-79
      D: 60-69
      F: <60
    """
    if not isinstance(score, int):
        raise TypeError("score must be int")
    if score < 0 or score > 100:
        raise ValueError("score out of range")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
