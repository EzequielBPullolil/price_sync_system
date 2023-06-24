from src.auth.exceptions import InvalidLoginCredentials
from src.user_role.models import User, UserRole
from datetime import datetime, timedelta
import jwt
import os


class LoginService:
    def __init__(self, session):
        self.__secret_key = os.environ["SECRET_KEY"]
        self.session = session

    def validate_credentials(self, login_credentials):
        """
          Describes User query response, only if the login_credentials are valid,
          else raises an DomainException

          :args
            - login_credentials(dict):
              - name(str): The new user name
              - password(str): The new user password
          :returns
            SQLAlchemy model instance

          :raises
            InvalidLoginCredentials
        """
        user = self.session.query(User).filter_by(
            name=login_credentials["name"]
        ).first()

        if (user == None or not user.check_password(login_credentials["password"])):
            raise InvalidLoginCredentials

        return user

    def generate_token(self, user):
        """
         Create a JWT with the id of the user and id of his role with the user
         of user
        """
        payload = {}
        payload["user_id"] = user.get_id()
        payload["role_id"] = self.__role_id(user)
        payload["exp"] = datetime.now() + timedelta(hours=12)
        return jwt.encode(payload, self.__secret_key, algorithm="HS256")

    def __role_id(self, user):
        """
          Describes de role_id of user
        """
        role = self.session.query(UserRole).filter_by(
            user_id=user.get_id()
        ).first()

        return role.role_id
