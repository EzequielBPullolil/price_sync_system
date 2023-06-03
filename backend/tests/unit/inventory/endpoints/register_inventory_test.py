class TestRegisterInventoryEndpoint:
    """
      This test verifies the correct operation of the Register inventory endpoint
      using the following test cases:
        - Valid endpoint request responds with status 201 and the inventory data
        - Request endpoint with barcode already registered responds with status code 400 and error information
        - Making an incomplete request to the endpoint responds with status 400 and error information
    """

    def test_valid_request_responds_with_status_201(self, client):
        """
          Request register inventory endpoint with valid inventory fields 
          responds with status 201 and inventory dao 
        """
        response = client.post("/inventory")

        assert response.status_code == 201

    def test_request_with_barcode_already_registered_responds_with_status_400(self, client, registered_barcode):
        """
          Verify if request the endpoint with already registered barcode responds with status 400 
          and error
        """
        response = client.post("/inventory", json={
            "barcode": registered_barcode
        })

        assert response.status_code == 400
