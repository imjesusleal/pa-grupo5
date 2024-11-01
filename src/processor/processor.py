import logging
import os
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor, as_completed

from ..images.images import Images


class IProcessor(ABC):

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


class Processor(IProcessor):
    def __init__(self, image_paths, output_dir, operation, num_threads):
        self.image_paths = image_paths
        self.output_dir = output_dir
        self.operation = operation
        self.num_threads = num_threads

    def process_single_image(self, img_path: str) -> str:
        image_processor = Images(img_path, self.output_dir)
        return image_processor.process(self.operation)

    def process_images(self) -> None:
        """Procesa las imágenes en paralelo utilizando concurrencia."""
        # Crea el directorio de salida si no existe
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
                        logging.info(f"Successfully processed {image_path} to {result}")
                    else:
                        logging.warning(f"Processing failed for {image_path}")
                except Exception as exc:
                    logging.error(f"{image_path} generated an exception: {exc}")
