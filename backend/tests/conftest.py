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
user_suject_fields = {
    "name": "zeki",
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
    user_suject = User(
        name=user_suject_fields["name"],
        password=user_suject_fields["password"]
    )

    session.add(user_suject)

    session.add(inventory_suject)
    session.commit()
    session.add(UserRole(
        user_id=user_suject.get_id(),
        role_id=2
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
def registered_user():
    session = DbSession()
    user = session.query(User).filter_by(
        name=user_suject_fields["name"]).first()
    user_id = str(user.id)
    user_role = session.query(UserRole).filter_by(
        user_id=user_id).first()
    session.close()
    return {
        "id": str(user_id),
        "name": user.name,
        "password": user_suject_fields["password"],
        "role_id": user_role.role_id
    }


@pytest.fixture()
def master_client(client, master_role_id):
    """
        Creates a client session with an master role_id
    """
    with client.session_transaction() as session:
        session['role_id'] = master_role_id

    yield client


@pytest.fixture()
def employee_client(client, employee_role_id):
    """
        Creates a client session with an employee role_id
    """
    with client.session_transaction() as session:
        session['role_id'] = employee_role_id

    yield client
