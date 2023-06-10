from src.exceptions import AlreadyRegisteredName
from src.user_role.models import User
from ..utils import UserDAO
from src.user_role.services import RoleAssigner


class UserCreator:
    def __init__(self, session):
        self.session = session
        self.role_assigner = RoleAssigner(session)

    def create(self, user_data):
        """
          Persist a new user in the db, assign it the passed
          role_id and return a user_dao, only if the name is
          available, else throw an exception

          :args
            - user_data(dict):
              - name(str): The new user name
              - password(str): The new user password
              - role_id(str): The new user role
          :returns
            UserDAO

          :raises
            AlreadyRegisteredName
        """
        if (self.session.query(User).filter_by(name=user_data["name"]).first() != None):
            raise AlreadyRegisteredName(user_data["name"])
        user = User(
            name=user_data["name"],
            password=user_data["password"]
        )

        self.session.add(user)
        self.session.commit()

        role_name = self.role_assigner.assing_role(user, user_data["role_id"])

        return UserDAO(user, role_name)
