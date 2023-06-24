from datetime import datetime
from src.exceptions import UnauthorizedUser
from src.user_role.role_enum import RolesID
import jwt
import os


class ValidateTokenService:
    def __init__(self, session):
        self.__secret_key = os.environ["SECRET_KEY"]
        self.session = session

    def validate_role_id(self, token, role_id):
        """
          Validates if the token passed is not expired token and
          have the role_id passed
          :args
            token - jwt

          :exceptions
            - UnauthorizedUser
        """
        decoded_token = jwt.decode(
            token,
            self.__secret_key,
            algorithms="HS256")

        self.__validate_token_expiration(decoded_token)
        self.__the_role_id_is_expected(decoded_token, role_id)

    def raises_error_if_role_is_not_employee_or_master(self, token):
        """
          Verify that the role_id of the token is equal to the role of master or employee,
          otherwise it throws an UnauthorizedUser exception

          :args
            token(str): A json web token

          :raises UnauthorizedUser
        """
        decoded_token = jwt.decode(
            token,
            self.__secret_key,
            algorithms="HS256")

        self.__validate_token_expiration(decoded_token)
        self.__validate_if_role_id_is_employee_or_master(decoded_token)

    def __validate_if_role_id_is_employee_or_master(self, decoded_token):
        """
          Check if the key "role_id" of the decoder toke is equal to master or employee,
          otherwise it throws the UnauthorizedUser exception

          :args
            -decoded_token(dict)
        """
        if 'role_id' not in decoded_token:
            raise UnauthorizedUser()

        if decoded_token["role_id"] == RolesID.EMPLOYEE.value or decoded_token["role_id"] == RolesID.MASTER.value:
            return

        raise UnauthorizedUser()

    def __validate_token_expiration(self, decoded_token):
        """
          Validates if the parsed decoded_token it is not expired
          :args
            - decoded_token(dict)
          :exceptions
            - UnauthorizedUser
        """
        if 'exp' in decoded_token:
            expiration_timestamp = decoded_token['exp']
            expiration_datetime = datetime.fromtimestamp(expiration_timestamp)
            current_datetime = datetime.now()
            if current_datetime > expiration_datetime:
                raise UnauthorizedUser()

    def __the_role_id_is_expected(self, decoded_token, role_id):
        """
          Validates if the parsed decoded_token have a valid
          user_id
          :args
            - decoded_token(dict)
          :exceptions
            - UnauthorizedUser
        """
        if 'role_id' not in decoded_token or decoded_token["role_id"] != role_id:
            raise UnauthorizedUser()
