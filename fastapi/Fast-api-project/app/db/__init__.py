from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import Depends
from app.db.base_class import Base

# Replace 'DATABASE_URL' with your actual database URL
DATABASE_URL = "postgresql://your_username:your_password@localhost/your_dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create tables on application startup
def init_db():
    Base.metadata.create_all(bind=engine)

init_db()  # This line initializes the database tables when the application starts