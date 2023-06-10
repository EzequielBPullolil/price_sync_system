from flask import session, request
from functools import wraps
from src.exceptions import UnauthorizedUser, InvalidUserField


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


def validate_create_user_fields(view_func):
    def wrapper_func(*args, **kwargs):
        fields = request.get_json()
        if (len(fields["name"]) < 3):
            raise InvalidUserField(fields["name"])
        if (len(fields["password"]) < 3):
            raise InvalidUserField(fields["password"])
        if (type(fields["role_id"]) != int):
            raise InvalidUserField(fields["role_id"])
        return view_func(*args, **kwargs)

    return wrapper_func
