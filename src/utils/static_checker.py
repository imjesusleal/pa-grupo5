import inspect
from functools import wraps


def static_validator(func):
    """
    Validador estatico para argumentos de funciones y de metodos.
    Permite decorar cualquier funcion o metodo y chequear que el tipo de dato enviado
    sea el mismo que el de las anotaciones.

    Args:
        func (function): recibe una funcion y la decora

    Returns:
        function: la funcion decorada

    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        type_check = inspect.get_annotations(func)

        sig = inspect.signature(func)
        params = list(sig.parameters.keys())

        if len(args) > 0 and params[0] in ("self", "cls"):
            func_args = args[1:]

        for i, (arg, expected_type) in enumerate(zip(func_args, type_check.values())):
            if not isinstance(arg, expected_type):
                raise TypeError(
                    f"El valor de posición {i+1} no es del tipo {expected_type}"
                )

        for kwarg_name, kwarg_value in kwargs.items():
            expected_type = type_check.get(kwarg_name)
            if expected_type and not isinstance(kwarg_value, expected_type):
                raise TypeError(
                    f"El valor '{kwarg_name}' no es del tipo {expected_type}"
                )

        return func(*args, **kwargs)

    return wrapper
