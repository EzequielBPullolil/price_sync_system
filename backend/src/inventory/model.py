from src.db import Base, engine
from sqlalchemy import Column, Integer, String, Numeric


class Inventory(Base):
    __tablename__ = 'inventorys'

    id = Column(Integer, primary_key=True)
    barcode = Column(String, unique=True)
    name = Column(String, unique=True)
    price = Column(Integer)
    stock = Column(Integer)

    def __init__(self, barcode, name, price, stock):
        self.barcode = barcode
        self.name = name
        self.price = price
        self.stock = stock


Base.metadata.create_all(engine)
