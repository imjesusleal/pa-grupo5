import os
from abc import ABC, abstractmethod
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed

from ..images.images import Images
from ..utils.logger import Logger
from ..utils.static_checker import static_validator


class IProcessor(ABC):
    """
    Interfaz que maneja el procesamiento concurrente y paralelo de imagenes.
    Es la encargada de crear una piscina de hilos y procesos de manera segura.

    Attributes:
        self: representacion interna de la instanciacion de la interfaz
        image_path (list[str]): una lista con las imagenes a procesar.
        output_dir (str): la representacion en cadena del directorio de salida
        operation (str): la operacion a aplicar al procesamiento de la imagen
        num_threads (int): numero de hilos o procesos a utilizar para el procesamiento.

    """

    @abstractmethod
    def process_single_image(self, img_path: str) -> str:
        """Procesa una sola imagen utilizando la clase Images.

        Args:
            self (IProcessor): La representacion interna de la instanciacion de la clase.
            img_path(str): La representacion en cadena de la ruta del filesystem.

        Returns:
            str: El path de la imagen procesada
        """

    @abstractmethod
    def process_images(self) -> None:
        """Maneja el procesamiento concurrente de las imágenes."""
        pass

    @abstractmethod
    def process_images_parallel(self) -> None:
        """Maneja el procesamiento paralelo de imagenes"""
        pass


class Processor(IProcessor):
    def __init__(
        self, image_paths: list[str], output_dir: str, operation: str, num_threads: int
    ):
        self.image_paths = image_paths
        self.output_dir = output_dir
        self.operation = operation
        self.num_threads = num_threads
        self._logger = Logger.get_logger()

    @static_validator
    def process_single_image(self, img_path: str) -> str:
        image_processor = Images(img_path, self.output_dir)
        return image_processor.process(self.operation)

    def process_images(self) -> None:
        """Procesa las imágenes en paralelo utilizando concurrencia."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # Usa ThreadPoolExecutor para procesar en paralelo
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            futures = {
                executor.submit(self.process_single_image, img_path): img_path
                for img_path in self.image_paths
            }
            for future in as_completed(futures):
                image_path = futures[future]
                try:
                    result = future.result()
                    if result:
                        self._logger.info(
                            f"Imagen procesada correctamente en {image_path} hacia {result}"
                        )
                    else:
                        self._logger.warning(
                            f"Procesamiento de imagen fallido para {image_path}"
                        )
                except Exception as exc:
                    self._logger.error(f"{image_path} se genero una excepcion: {exc}")

    def process_images_parallel(self) -> None:
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        with ProcessPoolExecutor(max_workers=self.num_threads) as executor:
            futures = {
                executor.submit(self.process_single_image, img_path): img_path
                for img_path in self.image_paths
            }
            for future in as_completed(futures):
                image_path = futures[future]
                try:
                    result = future.result()
                    if result:
                        self._logger.info(
                            f"Imagen procesada correctamente en {image_path} hacia {result}"
                        )
                    else:
                        self._logger.warning(
                            f"Procesamiento de imagen fallido para {image_path}"
                        )
                except Exception as exc:
                    self._logger.error(f"{image_path} se generó una excepción: {exc}")
