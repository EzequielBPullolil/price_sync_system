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


def jwt_required(f):
    """
        Validate that the jwt token exists in the request header
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        authorization_header = request.headers.get('Authorization')
        if authorization_header and authorization_header.startswith('Bearer '):
            token_jwt = authorization_header.split(' ')[1]
            return f(*args, **kwargs)
        raise UnauthorizedUser()
    return decorated_function


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
