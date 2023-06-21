from flask import Flask, make_response, jsonify
from src.inventory.routes import inventory_bp
from src.auth.routes import auth_bp
from src.auth.decorators import jwt_required
from src.exceptions import ApplicationLayerException, DomainException, UnauthorizedUser
import os


@inventory_bp.before_request
@jwt_required
def protected_routes():
    pass


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ["SECRET_KEY"]
    app.register_blueprint(inventory_bp)
    app.register_blueprint(auth_bp)

    @app.errorhandler(ApplicationLayerException)
    def applicatin_error_handler(error):
        return make_response(
            jsonify({
                "status": error.status,
                "message": error.message
            }), 400
        )

    @app.errorhandler(DomainException)
    def domain_error_handler(error):

        return make_response(
            jsonify({
                "status": error.status,
                "message": error.message
            }), 400
        )

    @app.errorhandler(UnauthorizedUser)
    def unauthorized_user_error_handler(error):
        return make_response(
            jsonify({
                "status": error.status,
                "message": error.message
            }), 401
        )

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
