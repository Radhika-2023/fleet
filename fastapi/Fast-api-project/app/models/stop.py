# app/models/stop.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.company import Company

class Stop(Base):
    id = Column(Integer, primary_key=True, index=True)
    stop_name = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    city = Column(String)
    district = Column(String)
    state = Column(String)
    pincode = Column(Integer)
    stop_owner_id = Column(Integer, ForeignKey('company.id'))
    additional_info = Column(String, nullable=True)

    # Relationships
    stop_owner = relationship("Company", back_populates="stops")
    routes = relationship("Route", secondary=route_stop_mapping, back_populates="stops")
