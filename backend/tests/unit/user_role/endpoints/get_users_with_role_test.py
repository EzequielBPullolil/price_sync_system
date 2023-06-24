class TestGetUsersWithRole:
    """
      This test verifies the correct operation of the 'get users with role' roles endpoint
      using the following test cases:
        - Valid endpoint request responds with status 200 and a list of user with their ids, name and the name of role they have
        - Send un registered role_id as url param return status 400 and json error information
    """

    def test_valid_endpoint_request_responds_with_status_200_and_user_role_list(self, employee_client, employee_role_id):
        """
          Verify if valid endpoint request responds with status 200 and a list of users

          Expected behavior:
              - The response should have a status code of 200
              - The response should contain a json with a list of all roles created
        """
        response = employee_client.get(f"/roles/{employee_role_id}")

        assert response.status_code == 200

    def test_request_endpoint_with_unregistered_role_id_responds_with_status_400_and_json_error(self, employee_client):
        """
          Verify if valid endpoint request responds with status 200 and a list of users

          Expected behavior:
              - The response should have a status code of 200
              - The response should contain a json with a list of all roles created
        """
        response = employee_client.get("/roles/999")

        assert response.status_code == 400
