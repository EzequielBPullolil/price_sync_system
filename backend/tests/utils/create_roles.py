
from src.user_role.models import Role


def create_roles(session):

    session.add(
        Role(id=1, name="master")
    )
    session.add(
        Role(id=2, name="employee")
    )
    session.commit()
