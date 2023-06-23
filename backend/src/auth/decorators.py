from flask import session, request
from functools import wraps
from src.exceptions import UnauthorizedUser, InvalidUserField
from .services.validate_token import ValidateTokenService
from src.db import DbSession


def role_required(role_id):
    """
        Verify that the token passed by the Authorization header has a role_id equal to the one passed by parameter
        if it is not the same, it throws the UnauthorizedUser exception
        :raises UnauthorizedUser
    """
    def decorator_func(view_func):
        @wraps(view_func)
        def wrapper_func(*args, **kwargs):
            session = DbSession()
            authorization_header = request.headers.get('Authorization')
            validate_token = ValidateTokenService(session)
            token_jwt = authorization_header.split(' ')[1]

            validate_token.validate_role_id(token_jwt, role_id)
            session.close()
            return view_func(*args, **kwargs)

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
