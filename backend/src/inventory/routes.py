from flask import Blueprint, request, jsonify, make_response

from .services.inventory_register import InventoryRegister
from .decorators import required_entrys
from src.db import DbSession
inventory_bp = Blueprint('inventory', __name__, url_prefix='/inventory')


@inventory_bp.route('/', methods=["POST"],  strict_slashes=False)
@required_entrys
def register_inventory():
    """
        Register an inventory in the database and
        create a log after validating the request fields

        :reqjson barcode: The inventory barcode

        :return: Success message and persisted inventoryDAO

        :rtype: json
    """
    db_session = DbSession()
    inventory_register = InventoryRegister(db_session)
    inventory_dao = inventory_register.register(request.get_json())

    db_session.close()
    return make_response(
        jsonify({
            "status": "Inventory created",
            "inventory": inventory_dao
        }), 201
    )
