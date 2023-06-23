from src.db import DbSession
from src.user_role.models import User, UserRole
from src.user_role.role_enum import RolesID
try:
    session = DbSession()
    user = User(
        name="Master",
        password="123456789"
    )
    session.add(user)
    session.commit()

    session.add(
        UserRole(
            role_id=RolesID.MASTER.value,
            user_id=user.get_id()
        )
    )
    session.commit()

    session.close()
    print("User with master role created, name Master, password 123456789")
except:
    print("User with master role created, name Master, password 123456789")
