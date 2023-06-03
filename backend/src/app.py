from flask import Flask
from src.inventory.routes import inventory_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(inventory_bp)
    return app
