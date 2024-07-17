from sqlalchemy import Column, ForeignKey, Table, orm, Integer
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class Base(DeclarativeBase):
    """Base database model."""
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
