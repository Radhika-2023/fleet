
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.company import Company
from app.models.company_staff import StaffRole

class CompanyStaff(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    middle_name = Column(String)
    last_name = Column(String)
    fleet_owner_id = Column(Integer, ForeignKey('company.id'))
    staff_role_id = Column(Integer, ForeignKey('staff_role.id'))
    email_id = Column(String, unique=True, index=True)
    phone = Column(Integer)
    otp_receive_time = Column(DateTime)
    additional_info = Column(String, nullable=True)

    # Relationships
    fleet_owner = relationship("Company", back_populates="staff")
    staff_role = relationship("StaffRole", back_populates="staff")
