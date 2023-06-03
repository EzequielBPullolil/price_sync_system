from flask import Blueprint, request, jsonify, make_response

from .services.inventory_register import InventoryRegister
from .services.inventory_fetcher import InventoryFetcher
from .decorators import required_inventory_entries
from src.db import DbSession
inventory_bp = Blueprint('inventory', __name__, url_prefix='/inventory')


@inventory_bp.route('/', methods=["POST"],  strict_slashes=False)
@required_inventory_entries
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


@inventory_bp.route('/<barcode>', methods=["GET"],  strict_slashes=False)
def fetch_by_barcode(barcode):
    """
        Finds a inventory by barcode and return 
        an inventory DAO
    """
    session = DbSession()
    inventory_fetcher = InventoryFetcher(session)
    inventory_dao = inventory_fetcher.find_by_barcode(barcode)
    session.close()
    return make_response(
        jsonify(inventory_dao.to_dict()), 200
    )
