from src.inventory.utils import InventoryDAO
from src.inventory.model import Inventory


class InventoryFetcher:
    def __init__(self, db_session):
        self.session = db_session

    def find_by_barcode(self, barcode):
        """
          Finds a inventory by barcode and return InventoryDAO,
          if the barcode is unregistered raise UnregisteredBarcode exception

          :args
            :barcode(str): The invetory barcode
          returns: InventoryDAO
        """
        inventory = self.session.query(
            Inventory).filter_by(barcode=barcode).first()
        return InventoryDAO(inventory)
