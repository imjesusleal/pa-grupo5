import os
from abc import ABC, abstractmethod

from .static_checker import static_validator


class IPath(ABC):
    """
    Interfaz para manejar el path correctamente.
    """

    @abstractmethod
    def check_directorio(self, path: str) -> bool:
        pass


class Path(IPath):
    """Implementacion concreta de Path.

    Args:
        path (str): una cadena con la referencia del directorio el cual
        queremos investigar
    """

    def __init__(self, path: str = None):
        self.path = path

    @static_validator
    def check_directorio(self, path: str) -> bool:
        """Chequea si el directorio existe y retorna un booleano.

        Args:
            self (Path): la representacion interna de la clase instanciada
            path (str): una cadena con la referencia del directorio el cual
        queremos investigar

        Returns:
            bool: true si el directorio enviado existe, false sino.
        """

        if not os.path.exists(path):
            return False
        self.path = path
        return True
