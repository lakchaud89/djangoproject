
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Region(Base):
    __tablename__='region'
    region_id = Column(Integer, primary_key=True)
    region_name = Column(String)
    state = Column(String)
    metro = Column(String)
    county = Column(String)
