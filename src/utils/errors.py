class ErrorHandler(Exception):
    """
    Manejo genero de excepciones. Hay que darle una pulida para generar
    errores customizados. Queda como un TODO dependiendo del tiempo.

    Args:
        exception (Exception): una excepcion atrapada por algun mal uso de la aplicacion.
    """

    def __init__(self, exception: Exception):
        self.exception: Exception = exception
        self.error_type = type(exception)

    def raise_exception(self):
        """
        Levanta el tipo de excepcion atrapada en la ejecucion del programa.
        Levanta la excepcion del tipo correcta, pero deberia devolver un mensaje customizado.
        """
        raise self.error_type(self.exception).with_traceback(
            self.exception.__traceback__
        )
