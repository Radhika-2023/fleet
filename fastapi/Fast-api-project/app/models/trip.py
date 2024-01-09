# app/models/trip.py
from sqlalchemy import Column, Integer, String, JSON, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.vehicle import Vehicle
from app.models.route import Route
from app.models.company_staff import CompanyStaff


class Trip(Base):
    id = Column(Integer, primary_key=True, index=True)
    trip_name = Column(String, index=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    route_id = Column(Integer, ForeignKey('route.id'))
    schedule_days = Column(JSON)
    start_time = Column(Time)
    end_time = Column(Time)
    driver_id = Column(Integer, ForeignKey('company_staff.id'))
    conductor_id = Column(Integer, ForeignKey('company_staff.id'))
    additional_info = Column(JSON, nullable=True)

    # Relationships
    vehicle = relationship("Vehicle", back_populates="trips")
    route = relationship("Route", back_populates="trips")
    driver = relationship("CompanyStaff", foreign_keys=[driver_id], back_populates="trips_as_driver")
    conductor = relationship("CompanyStaff", foreign_keys=[conductor_id], back_populates="trips_as_conductor")
