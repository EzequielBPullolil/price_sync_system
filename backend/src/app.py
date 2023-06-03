from flask import Flask, make_response, jsonify
from src.inventory.routes import inventory_bp
from src.exceptions import ApplicationLayerException, DomainException


def create_app():
    app = Flask(__name__)

    app.register_blueprint(inventory_bp)

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

    return app
