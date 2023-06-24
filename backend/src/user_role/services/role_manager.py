from src.exceptions import DomainException
from ..models import Role, UserRole, User
from src.auth.utils import UserDAO
from sqlalchemy import select
from src.exceptions import UnregisteredRole


class RoleManager:
    def __init__(self, session):
        self.session = session

    def find_all_roles(self):
        """ 
          Returns a list with all available roles,
          if there is no role it returns an empty list 
          :returns [Role]
        """
        roles = []
        query = self.session.query(Role).all()
        for role in query:
            roles.append(role.to_dict())
        return roles

    def find_all_user_with_role(self, role_id):
        """
            Returns a list with all the users that have 
            the role passed by parameter, if there is 
            no user with the passed role_id it returns an empty list
            :args
                role_id(int): The role id
            :returns [UserDAO]
            :raises UnregisteredRole
        """
        users = []
        role = self.session.query(Role).filter_by(id=role_id).first()
        if (role == None):
            raise UnregisteredRole(role_id)
        query = select(UserRole.user_id).where(UserRole.role_id == role_id)
        users_id = self.session.execute(query).fetchall()
        user_ids = [user[0] for user in users_id]

        for user_id in user_ids:
            user = self.session.query(User).filter_by(id=user_id).first()
            user_dao = UserDAO(user, role.name)
            users.append(user_dao.to_dict())
        return users

    def find_user_role(self, user):
        """
            Finds the role of user passed and return
            the role instance

            :args
                user(User): The user to look up role

            :returns
                Role
        """
        role_id = self.session.query(UserRole.role_id).filter_by(user_id=user.get_id()).first()

        role = self.session.query(Role).filter_by(id=role_id[0]).first()
        return role
