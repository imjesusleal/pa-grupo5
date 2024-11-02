import logging
import os
from abc import ABC
from logging.handlers import RotatingFileHandler
from typing import Type


class ILogger(ABC):
    """
    Interfaz singleton para el logger de operaciones.
    """

    @classmethod
    def get_logger(cls, name: str) -> Type["ILogger"]:
        """
        Chequea si existe una instancia creada. Si existe la retorna, sino la configura y la retorna:

        Args:
            name (str): El nombre del archivo, hardcodeado en _logger

        Returns:
            ILogger: la representacion creada de la interfaz.
        """
        pass

    @classmethod
    def _configure_logger(cls, name: str) -> Type["ILogger"]:
        """
        Funcion de configuracion de la interfaz de loggeo.

        Args:
            name (str): El nombre del archivo, hardcodeado en _logger

        Returns:
            ILogger: la representacion creada de la interfaz.
        """
        pass


class Logger(ILogger):
    _instance = None
    _ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _LOG_DIR = os.path.join(_ROOT, "logs")
    _LOG_FILE = os.path.join(_LOG_DIR, "_logger")

    @classmethod
    def get_logger(cls, name="_logger"):
        if cls._instance is None:
            cls._instance = cls._configure_logger(name)
        return cls._instance

    @classmethod
    def _configure_logger(cls, name: str):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        os.makedirs(cls._LOG_DIR, exist_ok=True)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        file_handler = RotatingFileHandler(
            cls._LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=5
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger
