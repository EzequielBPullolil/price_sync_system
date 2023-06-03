from flask import Blueprint
inventory_bp = Blueprint('inventory', __name__, url_prefix='/inventory')


@inventory_bp.route('/', methods=["POST"],  strict_slashes=False)
def register_inventory():
    """
        Register an inventory in the database and
        create a log after validating the request fields

        :reqjson barcode: The inventory barcode

        :return: Success message and persisted inventoryDAO

        :rtype: json
    """
    return {}, 201
