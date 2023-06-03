from src.exceptions import AlreadyRegisteredBarcode
from src.inventory.model import Inventory


class InventoryRegister:

    def __init__(self, db_session) -> None:
        self.session = db_session

    def register(self, inventory_data):
        """
            Persist and return the inventory
            with the fields passed by parameter

            Args: 
                inventory_data(InventoryFields)
                    - barcode(str): The Inventory barcode

            Returns: InventoryDAO
            Raises: AlreadyRegisteredBarcode
        """
        self.__is_barcode_avaible(inventory_data["barcode"])
        inventory = Inventory(
            barcode=inventory_data["barcode"],
            price=inventory_data["price"],
            stock=inventory_data["stock"],
            name=inventory_data["name"],

        )
        self.session.add(
            inventory
        )
        self.session.commit()
        return {
            "barcode": inventory_data["barcode"]
        }

    def __is_barcode_avaible(self, barcode):
        """
            Raise exception if exist an product registered
            with the barcode pased 

            Raises: AlreadyRegisteredBarcode
        """
        query = self.session.query(Inventory).filter_by(
            barcode=barcode
        ).first()
        if (query != None):
            raise AlreadyRegisteredBarcode(barcode)
