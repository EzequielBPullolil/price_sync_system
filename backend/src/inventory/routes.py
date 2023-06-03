from flask import Blueprint
inventory_bp = Blueprint('inventory', __name__, url_prefix='/inventory')


@inventory_bp.route('/', methods=["POST"],  strict_slashes=False)
def register_inventory():
    return {}, 201
