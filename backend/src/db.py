from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import os

engine = create_engine(os.environ["DATABASE_URI"])

DbSession = sessionmaker(engine)
Base = declarative_base()
