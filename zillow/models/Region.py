
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from models.base import Base
import models

class Region(Base):
    from models.MedianRent import MedianRent
    __tablename__='region'

    region_id = Column(Integer, primary_key=True)
    region_name = Column(String)
    state = Column(String)
    metro = Column(String)
    county = Column(String)
    rents = relationship("MedianRent", order_by=MedianRent.rent_id, back_populates="regions")

#Region.rents = relationship("MedianRent", order_by=MedianRent.rent_id, back_populates="region")
