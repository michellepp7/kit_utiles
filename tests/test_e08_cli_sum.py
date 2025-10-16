import pytest
from src.paquete_proyecto.cli import main

def test_main(capsys):
    main(["prog", "1,2,3"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "6.0"

def test_main_sin_argumentos(capsys):
    main(["prog"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "0"

    