class TestLoginEndpoint:
    """
     This test verifies the correct operation of the login endpoint
     using the following test cases:
       - Valid endpoint request responds with status 200 and login information
       - Request endpoint with unregistered user responds with status code 400
       - Making an incomplete request to the endpoint responds with status 400 and error information
       - Request endpoint with registered name and invalid password return status 400 


    A valid request consists of
        - That the user of the session has sufficient privileges to create a user, these are role master or admin 
        - Valid reqbody
          * name: Not registered name and length > 3
          * password: String length > 8
   """

    def test_valid_request_responds_with_status_200_and_login_information(self, client, registered_user):
        """
            Verify that sending a valid request to the 'login' endpoint responds
            with a status code of 200 and user_id

            Expected behavior:
                - The response should have a status code of 200
                - The response should contain a status, message and user_id
        """
        response = client.post('/auth/login', json={
            "name": registered_user["name"],
            "password": registered_user["password"]
        })

        assert response.status_code == 200

        login_information = response.get_json()

        assert login_information["status"] == "success"
        assert login_information["message"] == "Successful login"
        assert login_information["user_id"] == registered_user["id"]
