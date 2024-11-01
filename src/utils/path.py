import os
from abc import ABC, abstractmethod

from .static_checker import static_validator


class IPath(ABC):
    """
    Interfaz para manejar el path correctamente.
    """

    @abstractmethod
    def check_directory(self, path: str) -> bool:
        """Chequea si el directorio existe y retorna un booleano.

        Args:
            self (IPath): La representacion interna de la clase instanciada
            path (str): Una cadena con la referencia del directorio el cual
        queremos investigar

        Returns:
            bool: True si el directorio enviado existe, False sino.
        """
        pass

    @abstractmethod
    def change_directory(self) -> None:
        """
        Cambia el directorio actual hacia el directorio especificado por el usuario.
        """
        pass


class Path(IPath):
    """
    Implementacion concreta de Path.

    Args:
        path (str): una cadena con la referencia del directorio el cual
        queremos investigar
    """

    def __init__(self, path: str = None):
        self.__path: str = path
        self.__images: list[str] = []

        if not self.__path:
            self.__path = Path(".")

    @property
    def path(self) -> str:
        """
        Una cadena con la referencia del directorio el cual
        queremos investigar
        """
        return self.__path

    @property
    def images(self) -> list[str]:
        """
        La representacion de los nombres de las imagenes seleccionadas
        """
        return self.__images

    @static_validator
    def check_directory(self, path: str) -> bool:
        if not os.path.exists(path):
            return False
        self.__path = path
        return True

    def change_directory(self) -> None:
        os.chdir(self.path)
