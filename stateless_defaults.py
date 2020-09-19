from typing import Callable, Type, Tuple
from inspect import signature
from functools import wraps
from collections import deque


def stateless_defaults(*, supported_types: Tuple[Type] = (dict, list, deque, set)):
    def wrapper(func: Callable):
        @wraps(func)
        def wrapped(*args, **kwargs):
            func_signature = signature(func)
            bound_arguments = func_signature.bind(*args, **kwargs)
            for parameter in func_signature.parameters.values():
                if parameter.name in bound_arguments.arguments:
                    continue
                # If no argument was provided for this parameter, the parameter must have a default value.
                # Otherwise the `bind` call would have raised a `TypeError` for the missing argument.
                if not isinstance(parameter.default, supported_types):
                    # The default value is not a supported mutable collection and so it should not be overwritten.
                    continue
                bound_arguments.arguments[parameter.name] = type(parameter.default)()
            return func(*bound_arguments.args, **bound_arguments.kwargs)
        return wrapped
    return wrapper
