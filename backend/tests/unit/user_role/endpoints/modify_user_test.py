class TestModifyUser:
    """
      This test verifies the correct operation of the 'modify_user' user endpoint
      using the following test cases:
        - Valid endpoint request responds with status 200 and the UserDAO of modified user
        - Send unregistered user_id as url param return status 400 and json error information
        - Request with unauthorized user return status 400 and json error information
    """

    def test_valid_endpoint_request_responds_with_status_200_and_user_role_list(self, master_client, employee_user):
        """
          Verify if valid endpoint request responds with status 200 and a list of users

          Expected behavior:
              - The response should have a status code of 200
              - The response should contain a json with a list of all roles created
        """
        response = master_client.put(f"/users/{employee_user['id']}", json={
            "name": "new name",
            "password": "Ezequiel2"
        })

        assert response.status_code == 200
        json_response = response.get_json()
        user = json_response["user"]
        assert user["name"] == "new name"
        assert user["id"] == employee_user['id']

    def test_request_endpoint_with_unregistered_user_id_responds_with_status_400_and_json_error(self, master_client):
        """
          Verify if valid endpoint request responds with status 200 and a list of users

          Expected behavior:
              - The response should have a status code of 200
              - The response should contain a json with a list of all roles created
        """

        response = master_client.put("/users/999", json={
            "name": "new name",
            "password": "Ezequiel2"
        })

        assert response.status_code == 400

    def test_request_with_unauthorized_user_responds_with_status_400_and_json_error(self, client):
        """
          Verify if valid endpoint request responds with status 200 and a list of users

          Expected behavior:
              - The response should have a status code of 200
              - The response should contain a json with a list of all roles created
        """

        response = client.put("/users/1", json={
            "name": "new name",
            "password": "Ezequiel2"
        })

        assert response.status_code == 401
