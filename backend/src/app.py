from flask import Flask, make_response, jsonify, session
from src.inventory.routes import inventory_bp
from src.user.routes import user_bp, auth_bp
from src.exceptions import ApplicationLayerException, DomainException, UnauthorizedUser


def create_app():
    app = Flask(__name__)
    app.secret_key = 'my-secret-key'
    app.register_blueprint(inventory_bp)
    app.register_blueprint(user_bp)
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
