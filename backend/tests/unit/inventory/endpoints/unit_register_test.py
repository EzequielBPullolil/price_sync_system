class TestRegisterInventoryEndpoint:
    """
      This test verifies the correct operation of the Register inventory endpoint
      using the following test cases:
        - Valid endpoint request responds with status 201 and the inventory data
        - Request endpoint with barcode already registered responds with status code 400 and error information
        - Making an incomplete request to the endpoint responds with status 400 and error information
    """
    valid_request_fields = {
        "barcode": "nonregisteredbarcode",
        "name": "bon o bon",
        "price": 9000,
        "stock": 10
    }

    def test_valid_request_responds_with_status_201(self, client):
        """
          Request register inventory endpoint with valid inventory fields 
          responds with status 201 and inventory dao 
        """
        response = client.post("/inventory", json=self.valid_request_fields)

        assert response.status_code == 201
        json_response = response.get_json()
        assert json_response["status"] == "Inventory created"

        inventory_data = json_response["inventory"]
        assert inventory_data["barcode"] == self.valid_request_fields["barcode"]

    def test_request_with_barcode_already_registered_responds_with_status_400(self, client, registered_barcode):
        """
          Verify if request the endpoint with already registered barcode responds with status 400 
          and error
        """
        entry_invalid_barcode = self.valid_request_fields
        entry_invalid_barcode["barcode"] = registered_barcode
        response = client.post("/inventory", json=entry_invalid_barcode)

        assert response.status_code == 400
        json_response = response.get_json()
        assert json_response["status"] == "error"
        assert json_response["message"] == f"The barcode {registered_barcode} is already registered"

    def test_make_incomplete_request_to_endpoint_responds_with_status_400(self, client):
        """
          Makes a request to the endpoint without any of the necessary fields
        """
        necessary_fields = ["barcode", "name", "price", "stock"]

        for field_to_delete in necessary_fields:
            request_body = self.valid_request_fields
            del request_body[field_to_delete]
            response = client.post("/inventory", json=request_body)

            assert response.status_code == 400