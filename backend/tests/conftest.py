from src.app import create_app
from src.db import DbSession
from src.inventory.model import Inventory
import pytest
from sqlalchemy import text

inventory_suject_fields = {
    "price": 9999,
    "stock": 10,
    "name": "inventory_test_suject",
    "barcode": "fixture_registered_barcode"
}


def pytest_configure():
    """
        Delete all database rows 
        and create inventory subject
    """
    session = DbSession()

    session.execute(
        text("DELETE FROM inventorys")
    )
    inventory_suject = Inventory(
        barcode=inventory_suject_fields["barcode"],
        name=inventory_suject_fields["name"],
        price=inventory_suject_fields["price"],
        stock=inventory_suject_fields["stock"],

    )
    session.add(inventory_suject)
    session.commit()


@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture()
def inventory_suject() -> dict:
    return inventory_suject_fields


@pytest.fixture()
def registered_barcode():
    return inventory_suject_fields["barcode"]
