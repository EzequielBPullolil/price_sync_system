from src.exceptions import DomainException
from ..models import Role, UserRole


class RoleAssigner:
    def __init__(self, session):
        self.session = session

    def assing_role(self, user_query_response, role_id):
        """
            Assigns the role passed to the user and returns the name of the role
        """
        role = self.__find_role_by_ir_or_raises(role_id)
        
        self.session.add(UserRole(user_query_response.id, role_id))
        self.session.commit()
        return role.name
    
    def __find_role_by_ir_or_raises(self, id):
        role = self.session.query(Role).filter_by(id=id).first()

        if (role == None):
            raise DomainException(f"Non exist role with id {id}")
        
        return role