import logging
import os
from abc import ABC, abstractmethod

from PIL import Image


class IImages(ABC):

    @abstractmethod
    def process(self, operation: str) -> str | None:
        """Procesa la imagen de acuerdo a la operación especificada.

        Args:
            self (IImage): La representacion interna de la instanciacion de la clase.
            operation (str): La operacion a realizarse

        Returns:
            str | None: Devuelve la representacion en cadena de la direccion donde estan las
            imagenes procesadas.
        """
        pass

    @abstractmethod
    def resize(self, imag: list[str], size: tuple[int, int]) -> Image:
        """Redimensiona la imagen al tamaño especificado.

        Args:
            self (IImage): La representacion interna de la instanciacion de la clase.
            image (Image): La representacion de la imagen a ser procesada.
            size (tuple): Una tupla con el tamaño y la anchura para redimencionar la imagen en los ejes x,y.

        Returns:
            Image: Devuelve la imagen procesada.
        """
        pass

    @abstractmethod
    def grayscale(self, img: Image) -> Image:
        """
        Procesa y le cambia la escala de grises.

        Args:
            self (IImage): La representacion interna de la instanciacion de la clase.
            image (Image): La representacion de la imagen a ser procesada.

        Returns:
            Image: Devuelve la imagen procesada.
        """

    @abstractmethod
    def save_image(self, img: Image):
        """Guarda la imagen en el directorio de salida.

        Args:
            self (IImage): La representacion interna de la instanciacion de la clase.
            image (Image): La representacion de la imagen a ser procesada.

        Returns:
            str | None: Devuelve la representacion en cadena de la direccion donde estan las
            imagenes procesadas.

        """


class Images(IImages):
    def __init__(self, image_path: str, output_dir: str):
        self.image_path = image_path
        self.output_dir = output_dir

    def process(self, operation: str) -> str | None:
        try:
            with Image.open(self.image_path) as img:
                if operation == "resize":
                    img = self.resize(img)
                elif operation == "grayscale":
                    img = self.grayscale(img)
                output_path = self.save_image(img)
                logging.info(f"Imagen procesada {self.image_path} -> {output_path}")
                return output_path
        except Exception as e:
            logging.error(f"Error en procesamiento {self.image_path}: {e}")
            return None

    def resize(self, img: Image, size=(800, 600)) -> Image:
        return img.resize(size)

    def grayscale(self, img: Image) -> Image:
        return img.convert("L")

    def save_image(self, img: Image) -> str:
        output_path = os.path.join(self.output_dir, os.path.basename(self.image_path))
        img.save(output_path)
        return output_path
