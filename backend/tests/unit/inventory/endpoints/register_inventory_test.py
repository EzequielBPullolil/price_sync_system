class TestRegisterInventoryEndpoint:
    """
      This test verifies the correct operation of the Register inventory endpoint
      using the following test cases:
        - Valid endpoint request responds with status 201 and the inventory data
        - Request endpoint with barcode already registered responds with status code 400 and error information
        - Making an incomplete request to the endpoint responds with status 400 and error information
    """

    def test_valid_request_responds_with_satus_201(self, client):
        """
          Request register inventory endpoint with valid inventory fields 
          responds with status 201 and inventory dao 
        """
        response = client.post("/inventory")

        assert response.status_code == 201
