"""
Módulo cli.py
Mini utilidad de línea de comandos para sumar números separados por comas.

Uso:
    python -m src.cli 1,2,3,4
Salida:
    10.0
"""

import sys


def parse_numbers(arg: str) -> list[float]:
    """Convierte una cadena '1,2,3' en una lista de floats."""
    if not arg:
        return []
    return [float(x.strip()) for x in arg.split(",") if x.strip()]


def main(argv=None) -> int:
    """
    Función principal para ejecución CLI.
    Imprime la suma de los números pasados como argumento.
    """
    if argv is None:
        argv = sys.argv
    if len(argv) < 2:
        print(0)
        return 0
    nums = parse_numbers(argv[1])
    print(sum(nums))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
