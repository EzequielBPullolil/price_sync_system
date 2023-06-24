class TestGetUsersWithRole:
    """
      This test verifies the correct operation of the 'get users with role' roles endpoint
      using the following test cases:
        - Valid endpoint request responds with status 200 and a list of user with their ids, name and the name of role they have
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
        json = response.get_json()

        print(json)
