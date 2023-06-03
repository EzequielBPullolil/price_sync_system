class TestFetchByBarcodeInventoryEndpoint:
    """
      This test verifies the correct operation of the fetch by barcode inventory endpoint
      using the following test cases:
        - Valid endpoint request responds with status 200 and the inventory name, price and stock
        - Request endpoint with unregistered barcode responds with status code 400 and error information
    """

    def test_valid_endpoint_request_responds_with_status_200_and_inventory_dao(self, client, inventory_suject):
        """
          Verify if valid endpoint request responds with status 200 and inventory name, price and stock
        """
        response = client.get(
            f"/inventory/{inventory_suject['barcode']}")

        assert response.status_code == 200
        json_data = response.get_json()
        assert json_data["name"] == inventory_suject["name"]
        assert json_data["stock"] == inventory_suject["stock"]
        assert json_data["price"] == inventory_suject["price"]

    def test_request_with_unregistered_barcode_responds_with_status_code_400(self, client):
        """
          Verify if request endpoint with unregistered barcode responds with status code 400
        """
        unregistered_barcode = "unregistered_barcode_for_fetch_test"
        response = client.get(f"/inventory/{unregistered_barcode}")

        assert response.status_code == 400
