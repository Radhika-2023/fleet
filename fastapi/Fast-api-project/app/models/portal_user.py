
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime
from typing import Optional

class PortalUser(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    user_type_id = Column(Integer, ForeignKey('fleet_portal_user_type.id'))
    company_id = Column(Integer, ForeignKey('fleet_company.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    additional_info = Column(String, nullable=True)

    # Relationships
    user_type = relationship("FleetPortalUserType", back_populates="portal_users")
    company = relationship("FleetCompany", back_populates="portal_users")
