# app/models/vehicle.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.user import User
from app.models.service import Service
from app.models.company import Company

class Vehicle(Base):
    id = Column(Integer, primary_key=True, index=True)
    vehicle_number = Column(String, unique=True, index=True)
    vehicle_description = Column(String)
    permit_number = Column(String)
    capacity = Column(Integer)
    pos_id = Column(Integer, ForeignKey('user.id'))
    gps_id = Column(String)
    service_id = Column(Integer, ForeignKey('service.id'))
    fleet_owner_id = Column(Integer, ForeignKey('company.id'))
    additional_info = Column(String, nullable=True)

    # Relationships
    pos = relationship("User", back_populates="vehicles")
    service = relationship("Service", back_populates="vehicles")
    fleet_owner = relationship("Company", back_populates="vehicles")
