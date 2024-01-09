
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.user import User

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    email_id = Column(String, unique=True, index=True)
    profile_photo_url = Column(String, nullable=True)
    additional_info = Column(String, nullable=True)

    # Relationships
    user = relationship("User", back_populates="user")
