# app/models/fleet_portal_company_type.py
from sqlalchemy import Column, Integer, String
from app.db.base_class import Base

class CompanyType(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    additional_info = Column(String, nullable=True)
