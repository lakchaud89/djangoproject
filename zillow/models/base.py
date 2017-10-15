from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy import Table, Column, Integer, String, ForeignKey

@as_declarative()
class Base(object):
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)
