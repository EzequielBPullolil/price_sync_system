class TestPatchInventoryEndpoint:
    """
      This test verifies the correct operation of the patch inventory endpoint
      using the following test cases:
        - request endpoint with valid price 
        - Request endpoint with unregistered barcode responds with status code 400 and error information
    """

    def test_valid_endpoint_request_responds_with_status_200_and_inventory_dao(self, client, inventory_suject):
        """
          Verify if valid endpoint request responds with status 200 and inventory name, price and stock
        """
        updated_inventory = {
            "price": 909223,
            "stock": 0
        }
        response = client.patch(
            f"/inventory/{inventory_suject['barcode']}", json=updated_inventory)

        assert response.status_code == 200
        json_data = response.get_json()
        assert json_data["name"] == inventory_suject["name"]
        assert json_data["stock"] == updated_inventory["stock"]
        assert json_data["price"] == updated_inventory["price"]

    def test_request_with_unregistered_barcode_responds_with_status_code_400(self, client):
        """
          Verify if request endpoint with unregistered barcode responds with status code 400
        """
        unregistered_barcode = "unregistered_barcode_for_patch_test"
        response = client.patch(f"/inventory/{unregistered_barcode}")

        assert response.status_code == 400
