from src.exceptions import DomainException
from ..models import Role, UserRole


class RoleManager:
    def __init__(self, session):
        self.session = session

    def find_all_roles(self):
        """ 
          Returns a list with all available roles,
          if there is no role it returns an empty list 
          :returns  List of Roles
        """
        roles = []
        query = self.session.query(Role).all()
        for role in query:
            roles.append(role.to_dict())
        return roles
