
from src.inventory.model import Inventory
from src.inventory.utils import InventoryDAO
from src.common.helpers import BarcodeManager


class InventoryUpdater:
    def __init__(self, session) -> None:
        self.session = session
        self.barcode_manager = BarcodeManager(session)

    def patch(self, barcode, inventory_data):
        """
          Patch the price or stock of the inventory record in the database,
          if an inventory does not exist with the barcode, an error is thrown

          :barcode(str) - The barcode of the inventory to patch
          :inventory_data(dict): The inventory patch data 
            :price(int)
            :stock(int)

          :returns InventoryDAO 

          :raises UnregisteredBarcode
        """
        inventory_to_patch = self.barcode_manager.find_or_raises(barcode)
        inventory_to_patch.stock = inventory_data["stock"]
        inventory_to_patch.price = inventory_data["price"]

        self.session.commit()

        return InventoryDAO(inventory_to_patch)
