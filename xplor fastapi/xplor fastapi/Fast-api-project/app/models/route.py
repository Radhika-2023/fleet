# app/models/route.py
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

# Define the association table for many-to-many relationship
route_stop_mapping = Table(
    'route_stop_mapping',
    Base.metadata,
    Column('route_id', Integer, ForeignKey('route.id')),
    Column('stop_id', Integer, ForeignKey('stop.id'))
)

class Route(Base):
    id = Column(Integer, primary_key=True, index=True)
    route_description = Column(String)
    additional_info = Column(String, nullable=True)

    # Many-to-Many Relationship
    stops = relationship("Stop", secondary=route_stop_mapping, back_populates="routes")
