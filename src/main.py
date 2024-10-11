"""
main.py
=======================

El modulo principal de la aplicacion, punto de entrada.
"""

import os

from src.utils.path import Path


def main() -> None:
    """
    Funcion principal y punto de entrada para el programa.
    Es responsable de la logica de entrada y de la absorción de los argumentos
    pasados por linea de comando.
    """
    # positional_args = sys.argv

    # if len(positional_args) <= 1:
    #     sys.exit("No se ha enviado ningun directorio para chequear")

    path = Path()
    direct = os.path.abspath(".")
    print(direct)
    print(path.check_directorio(direct))


if __name__ == "__main__":
    main()
