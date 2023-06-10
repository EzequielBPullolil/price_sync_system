class TestCreateUserEndpoint:
    """
     This test verifies the correct operation of the create_user endpoint
     using the following test cases:
       - Valid endpoint request responds with status 201 and the UserDAO
       - Request endpoint with unauthorized user responds with status code 401
       - Making an incomplete request to the endpoint responds with status 400 and error information
       - Request endpoint with already registered name responds with status 400


    A valid request consists of
        - That the user of the session has sufficient privileges to create a user, these are role master or admin 
        - Valid reqbody
        * name: Not registered name and length > 3
        * password: String length > 8
        * role: valid role id
   """

    def test_valid_request_responds_with_status_201_and_user_dao(self, master_client, employee_role_id):
        """
        Verify that sending a valid request to the 'create_user' endpoint responds
        with a status code of 201 and a valid 'user dao' object.

        Expected behavior:
            - The response should have a status code of 201
            - The response should contain a 'user dao' object with the expected fields and values.
        """
        valid_reqbody = {
            "name": "Zeki",
            "password": "zxcvbnm",
            "role_id": employee_role_id
        }
        response = master_client.post("/user", json=valid_reqbody)
        assert response.status_code == 201
        json_response = response.get_json()

        assert json_response["status"] == "User created"
        response_user_dao = json_response["user"]
        assert response_user_dao["name"] == valid_reqbody["name"]
        assert response_user_dao["role_name"] == "employee"
        assert response_user_dao["id"] != None

    def test_request_endpoint_with_already_registered_name_responds_with_status_400_and_error_json(self, master_client, registered_user, employee_role_id):
        """
            Verify that sending a valid request with a registered name to the 'create_user' endpoint responds
            with a status code of 400 and an error JSON object.
            Scenario:
                - Attempting to create a user with a name that is already registered in the system.
            Expected behavior:
                - The response should have a status code of 400
                - The response should contain a 'json_error' object with the expected fields and values.
        """
        rebody_with_registered_name = {
            "name": registered_user["name"],
            "password": "zxcvbnm",
            "role_id": employee_role_id
        }
        response = master_client.post("/user",
                                      json=rebody_with_registered_name)
        assert response.status_code == 400
        json_response = response.get_json()

        assert json_response["status"] == "error"
        assert json_response["message"] == f"The name {registered_user['name']} is already registered"

    def test_request_endpoint_with_unauthorized_user_responds_with_status_code_401_and_error_json(self, employee_client, employee_role_id):
        """
            Verify that sending a valid request with a unauthorized user to the 'create_user' endpoint responds
            with a status code of 401 and an error JSON object.
            Scenario:
                - Attempting to create a user with a unauthorized user in the system.
            Expected behavior:
                - The response should have a status code of 401
                - The response should contain a 'json_error' 
        """
        valid_request = {
            "name": "Doc",
            "password": "zxcvbnm",
            "role_id": employee_role_id
        }
        response = employee_client.post("/user", json=valid_request)

        assert response.status_code == 401
