import argparse
import os
from abc import ABC, abstractmethod

from ..processor.processor import Processor
from ..utils.errors import ErrorHandler
from ..utils.path import Path


class IParser(ABC):

    @abstractmethod
    def parse_args(self):
        """Configura los argumentos de la CLI."""
        pass

    @abstractmethod
    def run(self) -> None:
        """Ejecuta la CLI para iniciar el procesamiento de imágenes."""
        pass


class Parser(IParser):
    def __init__(self):
        self.args = self.parse_args()
        self.__path: Path = Path()

    def parse_args(self):
        parser = argparse.ArgumentParser(
            description="CLI para procesar imágenes concurrentemente."
        )
        parser.add_argument(
            "dir_imagen", type=str, help="Directorio con imágenes de entrada."
        )
        parser.add_argument("dir_salida", type=str, help="Directorio de salida.")
        parser.add_argument(
            "--operation",
            type=str,
            choices=["resize", "grayscale"],
            required=True,
            help="Operación a realizar en las imágenes.",
        )
        parser.add_argument(
            "--threads", type=int, default=4, help="Número de hilos a utilizar."
        )
        parser.add_argument(
            "--check-dir",
            action="store_true",
            help="Verifica si el directorio es valido antes de procesar",
        )
        return parser.parse_args()

    def run(self):
        if self.args.check_dir:
            self.__path = Path(self.args.dir_imagen)
            print(self.__path.path)
            if not self.__path.check_directory(self.args.dir_imagen):
                with ErrorHandler(Exception) as e:
                    e.raise_exception()

        images = [
            os.path.join(self.args.dir_imagen, img)
            for img in os.listdir(self.__path.path)
            if img.endswith((".jpg", ".png", ".jpeg"))
        ]

        processor = Processor(
            image_paths=images,
            output_dir=self.args.dir_salida,
            operation=self.args.operation,
            num_threads=self.args.threads,
        )
        processor.process_images()
