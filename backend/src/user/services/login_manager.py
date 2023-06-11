from src.exceptions import InvalidLoginCredentials
from src.user_role.models import User


class LoginManager:
    def __init__(self, session):
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
