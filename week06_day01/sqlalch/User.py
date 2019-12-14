from sqlalchemy import Column, INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(50), nullable=False, unique=True)
