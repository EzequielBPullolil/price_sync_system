from src.db import DbSession
from src.user_role.models import Role
from src.user_role.role_enum import RolesID

try:
    session = DbSession()
    role = Role(
        id=RolesID.MASTER.value,
        name="master"
    )
    employee = Role(
        id=RolesID.EMPLOYEE.value,
        name="employee"
    )
    session.add(role)
    session.add(employee)
    session.commit()

    session.close()
    print("Roles created")
except:
    print("Roles created")
