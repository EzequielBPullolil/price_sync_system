from src.exceptions import DomainException
from ..models import Role, UserRole, User
from src.auth.utils import UserDAO
from sqlalchemy import select


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
        """
        users = []
        role = self.session.query(Role).filter_by(id=role_id).first()
        query = select(UserRole.user_id).where(UserRole.role_id == role_id)
        users_id = self.session.execute(query).fetchall()
        user_ids = [user[0] for user in users_id]
        for user_id in user_ids:
            user = self.session.query(User).filter_by(id=user_id).first()
            user_dao = UserDAO(user, role.name)
            users.append(user_dao.to_dict())
        return users
