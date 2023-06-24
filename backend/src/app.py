import os
from flask import Flask
from src.auth.decorators import jwt_required, required_employee_or_master_role
# Blueprints
from src.inventory.routes import inventory_bp
from src.auth.routes import auth_bp
from src.user_role.routes import roles_bp
# Exceptions
from src.exceptions import ApplicationLayerException, DomainException
from src.auth.exceptions import UnauthorizedUser
from src.error_handlers import applicatin_error_handler, domain_error_handler, unauthorized_user_error_handler


# Configure inventory_bp as protected route
@inventory_bp.before_request
@jwt_required
@required_employee_or_master_role
def protected_routes():
    pass


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ["SECRET_KEY"]
    app.register_blueprint(inventory_bp)
    app.register_blueprint(roles_bp)
    app.register_blueprint(auth_bp)

    app.register_error_handler(ApplicationLayerException, applicatin_error_handler)
    app.register_error_handler(DomainException, domain_error_handler)
    app.register_error_handler(UnauthorizedUser, unauthorized_user_error_handler)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
