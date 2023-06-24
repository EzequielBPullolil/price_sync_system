from flask import make_response, jsonify
from src.exceptions import ApplicationLayerException, DomainException
from src.auth.exceptions import UnauthorizedUser


def applicatin_error_handler(error):
    return make_response(
        jsonify({
            "status": error.status,
            "message": error.message
        }), 400
    )


def domain_error_handler(error):
    return make_response(
        jsonify({
            "status": error.status,
            "message": error.message
        }), 400
    )


def unauthorized_user_error_handler(error):
    return make_response(
        jsonify({
            "status": error.status,
            "message": error.message
        }), 401
    )
