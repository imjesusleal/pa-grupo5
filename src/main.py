"""
main.py
=======================

El modulo principal de la aplicacion, punto de entrada.
"""

import sys


def main() -> None:
    """
    Funcion principal y punto de entrada para el programa.
    Es responsable de la logica de entrada y de la absorción de los argumentos
    pasados por linea de comando.
    """
    print("Configuracion inicial del proyecto")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit("No has enviado parametros")
    main()
