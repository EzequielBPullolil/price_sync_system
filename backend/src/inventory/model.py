from src.db import Base, engine
from sqlalchemy import Column, Integer, String


class Inventory(Base):
    __tablename__ = 'inventorys'

    id = Column(Integer, primary_key=True)
    barcode = Column(String, unique=True)

    def __init__(self, barcode):
        self.barcode = barcode


Base.metadata.create_all(engine)
