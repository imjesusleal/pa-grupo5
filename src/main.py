"""
main.py
=======================
El modulo principal de la aplicacion, punto de entrada.
"""

# from PIL import Image

# from src.utils.path import Path
from .parser.parser import Parser


def main() -> None:
    """
    Funcion principal y punto de entrada para el programa.
    Es responsable de la logica de entrada y de solicitar el directorio
    con imagenes para procesar.
    """

    parser = Parser()
    parser.run()


if __name__ == "__main__":
    main()
