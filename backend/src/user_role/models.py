import uuid
from src.db import engine, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, name, password):
        self.name = name
        self.set_password(password)

    def get_id(self):
        return str(self.id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


class UserRole(Base):
    __tablename__ = 'user_role'
    user_id = Column(UUID(as_uuid=True),
                     ForeignKey('users.id'),
                     primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id'), primary_key=True)

    def __init__(self, user_id, role_id):
        self.user_id = user_id
        self.role_id = role_id

    def __repr__(self):
        return f"RoleUser(user_id={self.user_id}, role_id={self.role_id})"


Base.metadata.create_all(engine)
