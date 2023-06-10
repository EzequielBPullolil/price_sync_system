from flask import session
from functools import wraps
from src.exceptions import UnauthorizedUser


def role_required(role_id):
    def decorator_func(view_func):
        @wraps(view_func)
        def wrapper_func(*args, **kwargs):
            if 'role_id' in session and session['role_id'] == role_id:
                return view_func(*args, **kwargs)
            else:
                raise UnauthorizedUser()

        return wrapper_func

    return decorator_func
