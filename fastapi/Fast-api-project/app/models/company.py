# app/models/fleet_company.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.db.base_class import Base
from app.models.company import FleetPortalCompanyType
from sqlalchemy.orm import relationship

class Company(Base):
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    company_description = Column(String)
    domain = Column(String)
    company_type_id = Column(Integer, ForeignKey('fleet_portal_company_type.id'))
    email_id = Column(String, unique=True, index=True)
    contact = Column(Integer)
    pan = Column(String)
    permit_docs_url = Column(String, nullable=True)
    is_verified = Column(Boolean, default=False)
    upi_id = Column(String)
    additional_info = Column(String, nullable=True)

    # Relationships
    company_type = relationship("FleetPortalCompanyType", back_populates="companies")