import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
from models.base import Base

class MedianRent(Base):

        __tablename__='medianrent'

        rent_id = Column(Integer, primary_key = True)
        region_id = Column(Integer, ForeignKey('region.region_id'))
        yyyymm = Column(Integer)
        medianrent = Column(Integer)

        regions = relationship("Region", back_populates="rents")
