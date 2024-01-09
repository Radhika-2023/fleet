# app/routes/staffrole.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.staffrole import StaffRole
from app.db import get_db  # Assuming you have a function to get the database session

router = APIRouter()

@router.post("/staffroles/", response_model=StaffRole)
def create_staffrole(staffrole: StaffRole, db: Session = Depends(get_db)):
    db_staffrole = StaffRole(**staffrole.dict())
    db.add(db_staffrole)
    db.commit()
    db.refresh(db_staffrole)
    return db_staffrole

@router.get("/staffroles/{staffrole_id}", response_model=StaffRole)
def read_staffrole(staffrole_id: int, db: Session = Depends(get_db)):
    db_staffrole = db.query(StaffRole).filter(StaffRole.id == staffrole_id).first()
    if db_staffrole is None:
        raise HTTPException(status_code=404, detail="StaffRole not found")
    return db_staffrole
