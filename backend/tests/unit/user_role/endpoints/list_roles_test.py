class TestListRolesEndpoint:
    """
      This test verifies the correct operation of the 'list roles' roles endpoint
      using the following test cases:
        - Valid endpoint request responds with status 200 and a list of roles with their ids and names
        - Request endpoint with unregistered barcode responds with status code 400 and error information
    """

    def test_valid_endpoint_request_responds_with_status_200_and_inventory_dao(self, employee_client):
        """
          Verify if valid endpoint request responds with status 200 and a list of roles with their ids and names

          Expected behavior:
              - The response should have a status code of 200
              - The response should contain a json with a list of all roles created
        """
        response = employee_client.get("/roles")

        assert response.status_code == 200
        json = response.get_json()

        assert len(json) > 0
        assert json[0]["name"] != None
