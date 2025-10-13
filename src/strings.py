"""
Módulo strings.py
Funciones de texto para practicar el uso de pytest con fixtures y parametrización.
"""

import re
from collections import Counter

# Expresión regular simple para tokenizar palabras (sin tildes complicadas)
_TOKENIZER = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]+")


def word_count(text: str) -> dict[str, int]:
    """
    Cuenta la frecuencia de palabras en un texto.
    Ignora mayúsculas/minúsculas y signos de puntuación básicos.
    """
    tokens = _TOKENIZER.findall(text.lower())
    return dict(Counter(tokens))


_EMAIL = re.compile(r"^[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,10}$")


def validate_email(email: str) -> bool:
    """
    Valida un correo electrónico simple:
    usuario@dominio.tld donde:
      - usuario: letras, números, ., _, -
      - dominio: letras, números, -
      - tld: 2 a 10 letras
    """
    return bool(_EMAIL.match(email))
