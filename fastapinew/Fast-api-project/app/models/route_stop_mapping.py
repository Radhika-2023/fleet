# app/models/route_stop_mapping.py
from sqlalchemy import Column, Integer, Time, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.route import Route
from app.models.stop import Stop

class RouteStopMapping(Base):
    id = Column(Integer, primary_key=True, index=True)
    route_id = Column(Integer, ForeignKey('route.id'))
    stop_id = Column(Integer, ForeignKey('stop.id'))
    stop_number = Column(Integer)
    scheduled_arrival_time = Column(Time)
    additional_info = Column(JSON, nullable=True)

    # Relationships
    route = relationship("Route", back_populates="route_stop_mappings")
    stop = relationship("Stop", back_populates="route_stop_mappings")
