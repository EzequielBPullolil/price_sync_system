class TestRegisterInventoryEndpoint:
    """
      This test verifies the correct operation of the Register inventory endpoint
      using the following test cases:
        - Valid endpoint request responds with status 201 and the inventory data
        - Request endpoint with barcode already registered responds with status code 400 and error information
        - Making an incomplete request to the endpoint responds with status 400 and error information
        - Request endpoint missing token responds with status code 401 and error information

      For make request to this endpoint need have token than have a valid user_id and at least employee role
    """
    valid_request_fields = {
        "barcode": "nonregisteredbarcode",
        "name": "bon o bon",
        "price": 9000,
        "stock": 10
    }

    def test_valid_request_responds_with_status_201(self, employee_client):
        """
          Request register inventory endpoint with valid inventory fields 
          responds with status 201 and inventory dao 
        """
        response = employee_client.post(
            "/inventory", json=self.valid_request_fields)

        assert response.status_code == 201
        json_response = response.get_json()
        assert json_response["status"] == "Inventory created"

        inventory_data = json_response["inventory"]
        assert inventory_data["barcode"] == self.valid_request_fields["barcode"]

    def test_request_with_barcode_already_registered_responds_with_status_400(self, employee_client, registered_barcode):
        """
          Verify if request the endpoint with already registered barcode responds with status 400 
          and error
        """
        entry_invalid_barcode = self.valid_request_fields
        entry_invalid_barcode["barcode"] = registered_barcode
        response = employee_client.post(
            "/inventory", json=entry_invalid_barcode)

        assert response.status_code == 400
        json_response = response.get_json()
        assert json_response["status"] == "error"
        assert json_response["message"] == f"The barcode {registered_barcode} is already registered"

    def test_make_incomplete_request_to_endpoint_responds_with_status_400(self, employee_client):
        """
          Makes a request to the endpoint without any of the necessary fields
        """
        necessary_fields = ["barcode", "name", "price", "stock"]

        for field_to_delete in necessary_fields:
            request_body = self.valid_request_fields
            del request_body[field_to_delete]
            response = employee_client.post("/inventory", json=request_body)

            assert response.status_code == 400

    def test_request_with_missing_token_responds_with_status_401(self, client):
        """
        Verify that sending request with unauthorized user responds
        with a status code of 401 and error json

        Expected behavior:
            - The response should have a status code of 401
            - The response should contain a error json
        """
        response = client.post("/inventory", json={
            "barcode": "abarcodeForMissingToken",
            "name": "bon o bon",
            "price": 9000,
            "stock": 10
        })

        assert response.status_code == 401
