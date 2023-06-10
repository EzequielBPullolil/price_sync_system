
from src.user_role.models import Role
from src.user_role.role_enum import RolesID


def create_roles(session):

    session.add(
        Role(id=RolesID.MASTER.value, name="master")
    )
    session.add(
        Role(id=RolesID.EMPLOYEE.value, name="employee")
    )
    session.commit()
