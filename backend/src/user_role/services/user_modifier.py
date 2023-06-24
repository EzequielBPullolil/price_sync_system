from src.auth.exceptions import AlreadyRegisteredName
from src.user_role.models import User, UserRole
from src.auth.utils import UserDAO
from .role_manager import RoleManager


class UserModifierService:
    def __init__(self, session):
        self.session = session
        self.role_manager = RoleManager(session)

    def modify_by_id(self, user_id, newFields):
        """
          Modifies the user related to the user_id passed by parameter and returns a user_dao.
          in the case of passing the "name" field, the name must not be registered in the database,
          otherwise it will throw the AlreadyRegisteredName exception
          :args
            - newFields(dict):
              - name(str): The new user name
              - password(str): The new user password
              - role_id(str): The new user role
          :returns
            UserDAO

          :raises
            AlreadyRegisteredName
        """
        if (self.session.query(User).filter_by(name=newFields["name"]).first() != None):
            raise AlreadyRegisteredName(newFields["name"])

        user = self.session.query(User).filter_by(id=user_id).first()

        self.modify_name_if_can(user, newFields)
        self.modify_password_if_can(user, newFields)
        self.modify_role_id_if_can(user, newFields)
        self.session.commit()

        role = self.role_manager.find_user_role(user)
        return UserDAO(user, role.name)

    def modify_name_if_can(self, user, newFields):
        """
          Modify the name of user instance only if the 
          field name exist in newFields
          :args
            - user(User): User model instance
            - newFields(dict): The dict with the new fields of user
        """

        self.__modify_if_can(user, "name", newFields)

    def modify_password_if_can(self, user, newFields):
        """
          Modify the name of user instance only if the 
          field name exist in newFields
          :args
            - user(User): User model instance
            - newFields(dict): The dict with the new fields of user
        """

        self.__modify_if_can(user, "password", newFields)

    def modify_role_id_if_can(self, user, newFields):
        """
          Modifies the role_id of the user_role record that belongs to the user id
          :args
            - user(User): User model instance
            - newFields(dict): The dict with the new fields of user
        """
        user_role = self.session.query(UserRole).filter_by(user_id=user.get_id()).first()
        self.__modify_if_can(user_role, "role_id", newFields)
        self.session.commit()

    def __modify_if_can(self, obj, attribute, new_value):
        """
          Modify attribute if can, otherwise leaves the old value
        """
        if attribute in new_value:
            setattr(obj, attribute, new_value[attribute])
