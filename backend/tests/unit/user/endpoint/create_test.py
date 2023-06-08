class TestCreateUserEndpoint:
    """
     This test verifies the correct operation of the create_user endpoint
     using the following test cases:
       - Valid endpoint request responds with status 201 and the UserDAO
       - Request endpoint with non authorized user responds with status code 401
       - Making an incomplete request to the endpoint responds with status 400 and error information
       - Request endpoint with already registered name responds with status 400
   """

    def test_valid_request_responds_with_status_201_and_user_dao(self, client_with_session):
        """
        Verify that sending a valid request to the 'create_user' endpoint responds
        with a status code of 201 and a valid 'user dao' object.

        A valid request consists of
            - That the user of the session has sufficient privileges to create a user, these are role master or admin 
            - Valid reqbody
            * name: Not registered name and length > 3
            * password: String length > 8
            * role: valid role id
        Expected behavior:
            - The response should have a status code of 201
            - The response should contain a 'user dao' object with the expected fields and values.
        """
        valid_reqbody = {
            "name": "Zeki",
            "password": "zxcvbnm",
            "role_id": 1
        }
        response = client_with_session.post("/user", json=valid_reqbody)
        assert response.status_code == 201
        json_response = response.get_json()

        assert json_response["status"] == "User created"
        response_user_dao = json_response["user"]
        assert response_user_dao["name"] == valid_reqbody["name"]
        assert response_user_dao["role_name"] == "employee"
        assert response_user_dao["id"] != None
