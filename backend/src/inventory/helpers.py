from src.inventory.model import Inventory
from src.inventory.exceptions import UnregisteredBarcode


class BarcodeManager:
    def __init__(self, session):
        self.session = session

    def find_or_raises(self, barcode):
        """
          Search for the inventory by barcode in the database,
          if the inventory does not exist in the database it throws an UnregisteredBarcode

          :barcode(str) - The inventory barcode

          :return Inventory ORM model

          :raises UnregisteredBarcode
        """
        inventory = self.session.query(
            Inventory
        ).filter_by(barcode=barcode).first()

        if (inventory == None):
            raise UnregisteredBarcode(barcode)

        return inventory
