from flask import Blueprint, request, jsonify, make_response

from .services.inventory_register import InventoryRegister
from .services.inventory_fetcher import InventoryFetcher
from .services.inventory_updater import InventoryUpdater
from .decorators import required_inventory_entries
from src.db import DbSession
inventory_bp = Blueprint('inventory', __name__, url_prefix='/inventory')


@inventory_bp.route('/', methods=["POST"],  strict_slashes=False)
@required_inventory_entries
def register_inventory():
    """
        Register an inventory in the database and
        create a log after validating the request fields

        :reqjson inventory
                barcode(str): The inventory barcode
                price(int): The inventory price
                stock(int): The inventory stock
                name(str): The inventory name

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


@inventory_bp.route('/<barcode>', methods=["PATCH"],  strict_slashes=False)
def patch_inventory(barcode):
    """
        Update the price or stock of the inventory
        with the barcode passed by query
        :reqjson inventory
                barcode(str): The inventory barcode
                price(int): The inventory price
                stock(int): The inventory stock
                name(str): The inventory name

        :return: Success message and persisted inventoryDAO

        :rtype: json
    """
    session = DbSession()
    inventory_updater = InventoryUpdater(session)
    inventory_dao = inventory_updater.patch(
        barcode,
        request.get_json()
    )
    session.close()
    return make_response(
        jsonify(inventory_dao.to_dict()), 200
    )
