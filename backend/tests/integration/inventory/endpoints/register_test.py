from src.db import DbSession
from src.inventory.model import Inventory


class TestRegisterInventoryEndpointIntegration:
    session = DbSession()

    def test_valid_request_register_endpoint_persist_inventory_in_db(self, employee_client):
        """
          Verify if the valid request register inventory
          endpoint persist an inventory 
        """
        barcode = "integration_test_br_persist"
        response = employee_client.post("/inventory", json={
            "barcode": barcode,
            "name": "Sal",
            "price": 9000,
            "stock": 10
        })

        assert response.status_code == 201
        persisted_inventory = self.session.query(
            Inventory).filter_by(barcode=barcode).first()

        assert persisted_inventory != None
