import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from models.Region import Region

class MedianRent(Base):
        __tablename__='medianrent'
        rent_id = Column(Integer, primary_key = True)
        region_id = Column(Integer, ForeignKey(Region.region_id))
        yyyymm = Column(Integer)
        medianrent = Column(Integer)
