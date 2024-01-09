# app/models/service.py
from sqlalchemy import Column, Integer, String, Boolean
from app.db.base_class import Base

class Service(Base):
    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, index=True)
    reservation = Column(Boolean)
    additional_info = Column(String, nullable=True)
