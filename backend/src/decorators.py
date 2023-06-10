from flask import request
from functools import wraps

from src.exceptions import MissingRequiredField


def required_fields(required_fields):
    def decorator_func(view_func):
        @wraps(view_func)
        def wrapper_func(*args, **kwargs):
            for field in required_fields:
                if field not in request.get_json():
                    raise MissingRequiredField(field)

            return view_func(*args, **kwargs)

        return wrapper_func

    return decorator_func
