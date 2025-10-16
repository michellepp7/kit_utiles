"""
Módulo strings.py
Funciones de texto para practicar el uso de pytest con fixtures y parametrización.
"""

import re
from collections import Counter
import unicodedata

# Expresión regular simple para tokenizar palabras (sin tildes complicadas)
_TOKENIZER = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]+")

def _normalize_token(token: str) -> str:
    """Elimina tildes y normaliza el texto."""
    nfkd = unicodedata.normalize("NFD", token)
    return "".join([c for c in nfkd if unicodedata.category(c) != "Mn"])

def word_count(text: str) -> dict[str, int]:
    """
    Cuenta la frecuencia de palabras en un texto.
    Ignora mayúsculas/minúsculas y signos de puntuación básicos.
    Además elimina acentos (tildes).
    """
    tokens = _TOKENIZER.findall(text.lower())
    tokens = [_normalize_token(t) for t in tokens]
    return dict(Counter(tokens))


_EMAIL = re.compile(
    r"^[A-Za-z0-9._-]+@"        # usuario
    r"(?:[A-Za-z0-9-]+\.)+"     # uno o más subdominios
    r"[A-Za-z]{2,60}$"          # TLD 2–10 letras
)

def validate_email(email: str) -> bool:
    """
    Valida un correo electrónico simple:
    usuario@dominio.tld donde:
      - usuario: letras, números, ., _, -
      - dominio: letras, números, -
      - tld: 2 a 10 letras
    """
    return bool(_EMAIL.match(email))
