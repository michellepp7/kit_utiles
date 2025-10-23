"""
Módulo files.py
Ejemplo de lectura y escritura de líneas en archivos de texto.
"""

from pathlib import Path
from typing import Iterable

def save_lines(path: Path, lines: Iterable[str]) -> None:
    """
    Guarda una lista de cadenas en un archivo, una por línea.
    Crea las carpetas intermedias si no existen.
    No añade líneas en blanco adicionales.
    """
    path = Path(path)  # Asegura que sea un Path
    # 1) Crear la ruta si no existe (incluye subcarpetas)
    path.parent.mkdir(parents=True, exist_ok=True)

    # 2) Escribir las líneas en el archivo
    content = "\n".join(lines)
    path.write_text(content, encoding="utf-8")



def load_lines(path: Path) -> list[str]:
    """
    Lee todas las líneas de un archivo de texto y las devuelve como lista.
    Elimina los saltos de línea finales.
    """
    text = path.read_text(encoding="utf-8")
    if not text:
        return []
    return text.split("\n")
