from src.db import DbSession
from src.inventory.model import Inventory


class TestPatchInventoryEndpointIntegration:
    session = DbSession()

    def test_valid_request_patch_endpoint_update_row_inventory_in_db(self, employee_client, inventory_suject):
        """
          Verify if the valid request register inventory
          endpoint persist an inventory 
        """
        new_fields = {
            "price": 90020,
            "stock": 103
        }
        response = employee_client.patch(
            f"/inventory/{inventory_suject['barcode']}", json=new_fields)

        assert response.status_code == 200

        patched_inventory = self.session.query(
            Inventory).filter_by(barcode=inventory_suject['barcode']).first()

        assert patched_inventory != None
        assert patched_inventory.price == new_fields['price']
        assert patched_inventory.stock == new_fields['stock']
