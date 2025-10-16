import pytest
from src.paquete_proyecto.files import save_lines
from src.paquete_proyecto.files import load_lines


@pytest.fixture
def lineas():
    return ["uno", "dos", "tres"]


def test_save_and_load_lines(tmp_path, lineas):
    ruta = tmp_path / "archivo.txt"

    save_lines(ruta, lineas)
    resultado = load_lines(ruta)

    assert resultado == lineas


def test_vacio(tmp_path):
    ruta = tmp_path / "vacio.txt"
    ruta.touch()

    resultado = load_lines(ruta)

    assert resultado == []


