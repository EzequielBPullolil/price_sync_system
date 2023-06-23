from src.auth.services.login import LoginService
from src.app import create_app
from src.db import DbSession
from src.inventory.model import Inventory
from src.user_role.models import User, UserRole
import pytest
from src.user_role.role_enum import RolesID
from tests.utils.create_roles import create_roles
from tests.utils.reset_database import reset_database

inventory_suject_fields = {
    "price": 9999,
    "stock": 10,
    "name": "inventory_test_suject",
    "barcode": "fixture_registered_barcode"
}
employee_user_suject = {
    "name": "zeki",
    "password": "apassword"
}
master_user_suject = {
    "name": "zeki22",
    "password": "apassword"
}


def pytest_configure():
    """
        Delete all database rows 
        and create inventory subject
    """
    session = DbSession()
    reset_database(session)
    create_roles(session)
    inventory_suject = Inventory(
        barcode=inventory_suject_fields["barcode"],
        name=inventory_suject_fields["name"],
        price=inventory_suject_fields["price"],
        stock=inventory_suject_fields["stock"]
    )
    employee_user = User(
        name=employee_user_suject["name"],
        password=employee_user_suject["password"]
    )
    master_user = User(
        name=master_user_suject["name"],
        password=master_user_suject["password"]
    )
    session.add(employee_user)
    session.add(master_user)
    session.add(inventory_suject)
    session.commit()
    session.add(UserRole(
        user_id=employee_user.get_id(),
        role_id=RolesID.EMPLOYEE.value
    ))
    session.add(UserRole(
        user_id=master_user.get_id(),
        role_id=RolesID.MASTER.value
    ))
    session.commit()


@pytest.fixture
def app():
    app = create_app()
    app.config['SECRET_KEY'] = 'my-secret-key'
    app.config["TESTING"] = True
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture()
def inventory_suject() -> dict:
    session = DbSession()
    inventory = session.query(Inventory).filter_by(
        barcode=inventory_suject_fields["barcode"]).first()
    session.close()
    return {
        "price": inventory.price,
        "stock": inventory.stock,
        "name": inventory.name,
        "barcode": inventory.barcode
    }


@pytest.fixture()
def registered_barcode():
    return inventory_suject_fields["barcode"]


@pytest.fixture()
def master_role_id():
    return RolesID.MASTER.value


@pytest.fixture()
def employee_role_id():
    return RolesID.EMPLOYEE.value


@pytest.fixture()
def employee_user():
    session = DbSession()
    user = session.query(User).filter_by(
        name=employee_user_suject["name"]).first()
    user_id = str(user.id)
    user_role = session.query(UserRole).filter_by(
        user_id=user_id).first()
    session.close()
    return {
        "id": str(user_id),
        "name": user.name,
        "password": employee_user_suject["password"],
        "role_id": user_role.role_id
    }


@pytest.fixture()
def master_user():
    session = DbSession()
    user = session.query(User).filter_by(
        name=master_user_suject["name"]).first()
    user_id = str(user.id)
    user_role = session.query(UserRole).filter_by(
        user_id=user_id).first()
    session.close()
    return {
        "id": str(user_id),
        "name": user.name,
        "password": master_user_suject["password"],
        "role_id": user_role.role_id
    }


@pytest.fixture()
def master_client(client, master_jwt):
    """
        Creates a client session with an master role_id
    """
    with client:
        client.environ_base['HTTP_AUTHORIZATION'] = f'Bearer {master_jwt}'

        yield client


@pytest.fixture()
def employee_client(client, employee_jwt):
    """
        Creates a client with a token in Authorization
        header with a valid employee jwt
    """
    with client:
        client.environ_base['HTTP_AUTHORIZATION'] = f'Bearer {employee_jwt}'

        yield client


@pytest.fixture()
def employee_jwt(employee_user):
    session = DbSession()
    login_service = LoginService(session)
    user = session.query(User).filter_by(
        name=employee_user["name"]).first()
    return login_service.generate_token(user)


@pytest.fixture()
def master_jwt(master_user):
    session = DbSession()
    login_service = LoginService(session)
    user = session.query(User).filter_by(
        name=master_user["name"]).first()
    return login_service.generate_token(user)
