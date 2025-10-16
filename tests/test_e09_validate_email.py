import pytest
from src.strings import validate_email


@pytest.mark.parametrize("email", [
    "user@example.com",
    "nombre.apellido@dominio-es.org",
    "u_1-2@dominio.net"])

def test_validate_email_valido(email):
    assert validate_email(email) == True

@pytest.mark.parametrize("email", [
    "sin_arroba.com",
    "user@dominio.",
    "user@dominio.c"])

def test_validate_email_invalido(email):
    assert validate_email(email) == False


